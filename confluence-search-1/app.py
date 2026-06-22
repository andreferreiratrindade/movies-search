import json
from fastapi import FastAPI, Query
import chromadb
from chromadb.utils import embedding_functions
import ollama
from fastapi.middleware.cors import CORSMiddleware
from sentence_transformers import SentenceTransformer, CrossEncoder


app = FastAPI(title="Open Finance RAG Search API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows everything
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # Allows Content-Type, Authorization, etc.
)
MODEL_NAME = "all-MiniLM-L6-v2"
CROSS_ENCODER_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

print("Loading Cross-Encoder for contextual re-ranking...")
cross_encoder = CrossEncoder(CROSS_ENCODER_NAME)
# 1. Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)
collection = chroma_client.get_or_create_collection(name="open_finance", embedding_function=embedding_fn)

# 2. Configure Local Ollama Client
local_llm_client = ollama.Client(host="http://host.docker.internal:11434")

@app.get("/search")
async def search_and_answer(query: str = Query(..., description="The user's question"), limit: int = 30):
    # Step 1: Semantic search inside ChromaDB
    RETRIEVAL_POOL_SIZE = max(100, limit * 2)
    final_search_text = query
    expansion_prompt = f"""
    Você é um arquiteto de busca semântica e um Especialista Sênior em Open Finance Brasil, com domínio absoluto da infraestrutura técnica, manuais de APIs, segurança (FAPI/OAuth2) e de toda a regulamentação do Banco Central do Brasil (BCB) e do Conselho Monetário Nacional (CMN).

Sua tarefa é receber a pergunta conversacional de um usuário e transformá-la em uma consulta de busca altamente otimizada para bancos de dados vetoriais (Semantic Search) que indexam documentações técnicas e normativas oficiais.

Siga estas regras estritamente:
1. Remova ruídos conversacionais, saudações e palavras de preenchimento (ex: "olá", "por favor me explique", "como funciona").
2. Extraia as entidades principais, verbos de ação e jargões técnicos.
3. Expansão de Domínio Regulatório (Crucial): Traduza termos coloquiais para a nomenclatura oficial do BCB e do ecossistema Open Finance. (Exemplos: mapeie "pagamento" para "iniciação de transação de pagamento ITP", "banco" para "instituição participante", "autorização" para "consentimento").
4. Adicione sinônimos técnicos, siglas relevantes (ex: ITP, detentor de conta, transmissor de dados, receptor) e mencione agrupamentos lógicos (ex: Fase 1, Fase 2, APIs de Consents, Resources, Payments, Resolução Conjunta) que possam estar nos documentos originais para melhorar o 'recall'.
5. Mantenha o idioma original da pergunta.
6. RETORNE APENAS A CONSULTA REFINADA. Não adicione explicações, aspas, ou textos de introdução.

Pergunta original do usuário:
No contexto da regulamentação e infraestrutura do Open Finance Brasil, "{query}"

Consulta refinada:
    """
    try:
        response = local_llm_client.generate(
            model="gemma3",
            prompt=expansion_prompt,
            options={"temperature": 0.2, "max_tokens": 100}
        )
        final_search_text = response['response'].strip()
    except Exception as e:
        print(f"Query expansion failed, falling back. Error: {e}")

    results = collection.query(
        query_texts=[final_search_text],
        n_results=RETRIEVAL_POOL_SIZE
    )



    # Compile findings into standard context strings for the LLM
    context_chunks = []
    sources_used = []
    candidates = []

    if results and results['ids'] and len(results['ids'][0]) > 0:
        for i in range(len(results['ids'][0])):
            metadata = results['metadatas'][0][i] or {}
            doc_text = results['documents'][0][i]

            doc_url = metadata.get('url', 'URL não informada')
            doc_title = metadata.get('title', 'Documento Sem Título')
            candidates.append({
                "source_index": i + 1,
                "title": doc_title,
                "url": doc_url,
                "distances": results['distances'][0][i],
                "matched_context": doc_text

            })

    if not candidates:
        return {"query": final_search_text, "total_results_returned": 0, "results": []}

    # --- Stage 3: Cross-Encoder Re-ranking ---
    # Prepare pairs for the Cross-Encoder: [(Query, MovieText1), (Query, MovieText2), ...]
    cross_inputs = [[final_search_text, item["matched_context"]] for item in candidates]

    # Compute relevance scores (higher scores mean tighter semantic matching)
    re_rank_scores = cross_encoder.predict(cross_inputs)

    # Attach the new scores to our candidates
    for idx, score in enumerate(re_rank_scores):
        candidates[idx]["cross_encoder_score"] = float(score)

    # Sort candidates by the Cross-Encoder score in descending order (highest score first)
    sorted_candidates = sorted(candidates, key=lambda x: x["cross_encoder_score"], reverse=True)

    # Trim the results down to the final requested limit
    final_results = sorted_candidates[:limit]

    for i, item in enumerate(final_results):
        doc_title = item.get('title', 'Documento Sem Título')
        doc_url = item.get('url', 'URL não informada')

        sources_used.append({
            "source_index": i + 1,
            "title": doc_title,
            "url": doc_url,
            "distances": item.get('distances', 0)
        })
        context_snippet = f"Fonte [{i+1}]: {doc_title}\nURL: {doc_url}\nConteúdo: {doc_text}\n"
        context_chunks.append(context_snippet)

    # Combine all found documents into a single block
    full_context_str = "\n---\n".join(context_chunks) if context_chunks else "Nenhum documento encontrado no banco."

    # Step 2: Build the context-grounded prompt engineering template
    expansion_prompt = f"""Você é um arquiteto especialista no ecossistema do Open Finance Brasil.
Responda à pergunta do usuário utilizando estritamente as informações fornecidas no Contexto abaixo.

Regras Obrigatórias de Resposta:
1. Responda obrigatoriamente no idioma Português do Brasil (PT-BR).
2. Seja claro, objetivo e técnico.
3. Se a informação não puder ser extraída ou deduzida do contexto fornecido, diga textualmente: "Não encontrei essa informação na documentação extraída."
4. Ao final da resposta, cite explicitamente quais URLs (das fontes fornecidas no contexto) serviram de base para formular sua resposta.

---
CONTEXTO EXTRAÍDO DA DOCUMENTAÇÃO:
{full_context_str}
---

PERGUNTA DO USUÁRIO: {query}

RESPOSTA EM PT-BR (Lembre-se de citar as URLs das fontes utilizadas):"""

    # Step 3: Run Inference using gemma3 via Ollama Client
    try:
        response = local_llm_client.generate(
            model="gemma3",
            prompt=expansion_prompt,
            options={
                "temperature": 0.2
                # Removed max_tokens=100 to avoid cutting off long detailed technical answers
            }
        )
        ai_answer = response.get('response', '')
    except Exception as e:
        ai_answer = f"Erro ao processar resposta no modelo local Ollama: {str(e)}"

    return {
        "question": query,
        "question_refined": final_search_text,
        "ai_answer": ai_answer,
        "referenced_sources": sources_used
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
