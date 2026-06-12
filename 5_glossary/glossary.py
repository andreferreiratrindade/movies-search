import chromadb
from chromadb.utils import embedding_functions

chroma_client = chromadb.PersistentClient(path="./chroma_storage")
MODEL_NAME = "all-MiniLM-L6-v2"
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)

# Create a separate collection for your company knowledge base
glossary_collection = chroma_client.get_or_create_collection(
    name="glossary",
    embedding_function=embedding_fn
)

# Your business definitions
glossary_data = [
    {
        "term": "Sensedia",
        "definition": "Sensedia is a brazilian company based on Sao Paulo, Brazil. It's principal products are API management, Adaptive Governance and consulting service."
    },
    # You can add more company or product profiles here safely over time
]

ids = [item["term"].lower() for item in glossary_data] # e.g., 'sensedia'
documents = [item["definition"] for item in glossary_data]
metadatas = [{"term": item["term"]} for item in glossary_data]

glossary_collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print(f"Glossary populated! Total terms: {glossary_collection.count()}")
