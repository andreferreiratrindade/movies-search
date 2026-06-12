# search.py
import sys
from llama_index.core import VectorStoreIndex, Settings, PromptTemplate
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
import chromadb

# Configuração para conectar ao Ollama no Host a partir do Dev Container
HOST_OLLAMA_URL = "http://host.docker.internal:11434"

# Configuração dos modelos locais
Settings.llm = Ollama(model="llama3", base_url=HOST_OLLAMA_URL, request_timeout=120.0)
Settings.embed_model = OllamaEmbedding(model_name="mxbai-embed-large", base_url=HOST_OLLAMA_URL)

# Criamos um template de Prompt para garantir respostas estritamente em Português (PT-BR)
TEXT_QA_TEMPLATE_STR = (
    "As informações de contexto extraídas da documentação estão abaixo:\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Dada a informação de contexto e nenhuma outra informação prévia, "
    "responda à seguinte pergunta obrigatoriamente no idioma Português do Brasil (PT-BR).\n"
    "Seja claro, objetivo e técnico conforme a arquitetura do Open Finance.\n"
    "Se a informação não puder ser encontrada no contexto fornecido, diga textualmente: "
    "'Não encontrei essa informação na documentação extraída.'\n\n"
    "Pergunta: {query_str}\n"
    "Resposta em PT-BR:"
)

QA_PROMPT = PromptTemplate(TEXT_QA_TEMPLATE_STR)

def carregar_index_existente():
    db = chromadb.PersistentClient(path="./chroma_db_local")
    colecao_chroma = db.get_or_create_collection("open_finance_brasil_local")
    vector_store = ChromaVectorStore(chroma_collection=colecao_chroma)
    return VectorStoreIndex.from_vector_store(vector_store=vector_store)

def realizar_busca_semantica(pergunta_usuario: str):
    print("📚 Carregando index do banco de dados vetorial...")
    index = carregar_index_existente()

    # Inicializa o motor aplicando o nosso prompt customizado em PT-BR
    mecanismo_busca = index.as_query_engine(
        similarity_top_k=3,
        text_qa_template=QA_PROMPT  # <-- Injeta a instrução do idioma aqui
    )

    print(f"\n🔍 Consultando o modelo local: '{pergunta_usuario}'\n" + "-"*50)
    resposta = mecanismo_busca.query(pergunta_usuario)

    print("\n💡 Resposta Gerada pela IA Local (PT-BR):")
    print(resposta)

    print("\n📑 Fontes de Referência Utilizadas:")
    # Correção aplicada para evitar falhas de escopo nas variáveis do laço
    for no in resposta.source_nodes:
        score = no.score if no.score is not None else 0.0
        print(f"- Título: {no.metadata.get('title')} | URL: {no.metadata.get('url')} (Score: {score:.4f})")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        pergunta = " ".join(sys.argv[1:])
    else:
        pergunta = "Como funciona o ecossistema do Open Finance Brasil?"

    realizar_busca_semantica(pergunta)
