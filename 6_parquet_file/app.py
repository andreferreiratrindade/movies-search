import os
# Force the Hugging Face mirror network to bypass 429 rate limits
# os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from fastapi import FastAPI, Query
from sentence_transformers import SentenceTransformer, CrossEncoder
import chromadb
from chromadb.utils import embedding_functions

app = FastAPI(title="Sensedia Gateway Log Semantic Search API with Re-ranking")

# 1. Initialize Models
MODEL_NAME = "all-MiniLM-L6-v2"
CROSS_ENCODER_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

print("Loading Bi-Encoder for vector retrieval...")
bi_encoder = SentenceTransformer(MODEL_NAME)

print("Loading Cross-Encoder for contextual re-ranking...")
cross_encoder = CrossEncoder(CROSS_ENCODER_NAME)

# 2. Initialize Vector DB Client targeting enriched log structures
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)

# Switch targeted collection here
collection = chroma_client.get_collection(name="enriched_api_logs")

@app.get("/search")
async def search_logs(
    query: str = Query(..., description="Semantic query to look up within transaction traces"),
    limit: int = 5
):
    # --- Stage 1: Retrieve Candidates from ChromaDB ---
    RETRIEVAL_POOL_SIZE = max(25, limit * 2)

    results = collection.query(
        query_texts=[query],
        n_results=RETRIEVAL_POOL_SIZE
    )

    # Parse and safely structure metadata fields returning from enriched_api_logs
    candidates = []
    if results and results['ids'] and len(results['ids'][0]) > 0:
        for i in range(len(results['ids'][0])):
            meta = results['metadatas'][0][i] or {}
            candidates.append({
                "trace_id": results['ids'][0][i],
                "url": meta.get("url", "Unknown"),
                "method": meta.get("method", "Unknown"),
                "status_code": meta.get("status_code", 0),
                "app_name": meta.get("app_name", "Unknown"),
                "environment": meta.get("environment", "Unknown"),
                "bi_encoder_distance": results['distances'][0][i],
                "matched_context": results['documents'][0][i]
            })

    if not candidates:
        return {"query": query, "total_results_returned": 0, "results": []}

    # --- Stage 2: Cross-Encoder Re-ranking ---
    cross_inputs = [[query, item["matched_context"]] for item in candidates]
    re_rank_scores = cross_encoder.predict(cross_inputs)

    # Bind relevance weightings back to specific trace matches
    for idx, score in enumerate(re_rank_scores):
        candidates[idx]["cross_encoder_score"] = float(score)

    # Sort results with the highest similarity matching scores prioritized first
    sorted_candidates = sorted(candidates, key=lambda x: x["cross_encoder_score"], reverse=True)
    final_results = sorted_candidates[:limit]

    return {
        "query": query,
        "total_candidates_evaluated": len(candidates),
        "results_returned": len(final_results),
        "results": final_results
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
