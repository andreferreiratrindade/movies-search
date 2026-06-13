import json
from fastapi import FastAPI, Query
import chromadb
from chromadb.utils import embedding_functions
import ollama
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Open Finance RAG Search API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows everything
    allow_credentials=True,
    allow_methods=["*"],  # Allows GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # Allows Content-Type, Authorization, etc.
)
MODEL_NAME = "all-MiniLM-L6-v2"

# 1. Connect to ChromaDB
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)
collection = chroma_client.get_or_create_collection(name="open_finance", embedding_function=embedding_fn)

# 2. Configure Local Ollama Client
local_llm_client = ollama.Client(host="http://host.docker.internal:11434")

@app.get("/search")
async def search_and_answer(query: str = Query(..., description="The user's question"), limit: int = 5):
    # Step 1: Semantic search inside ChromaDB
    results = collection.query(
        query_texts=[query],
        n_results=limit
    )

    # Compile findings into standard context strings for the LLM
    context_chunks = []
    sources_used = []

    if results and results['ids'] and len(results['ids'][0]) > 0:
        for i in range(len(results['ids'][0])):


            metadata = results['metadatas'][0][i] or {}
            doc_text = results['documents'][0][i]
            doc_url = metadata.get('url', 'URL não informada')
            doc_title = metadata.get('title', 'Documento Sem Título')

            # Format raw matching details into a readable snippet for the prompt context
            context_snippet = f"Fonte [{i+1}]: {doc_title}\nURL: {doc_url}\nConteúdo: {doc_text}\n"
            context_chunks.append(context_snippet)

            # Track sources to send cleanly back in the JSON API output
            sources_used.append({
                "source_index": i + 1,
                "title": doc_title,
                "url": doc_url,
                "distance": results['distances'][0][i]
            })

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
        "ai_answer": ai_answer,
        "referenced_sources": sources_used
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
