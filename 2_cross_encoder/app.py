from fastapi import FastAPI, Query
from sentence_transformers import SentenceTransformer, CrossEncoder
import chromadb
from chromadb.utils import embedding_functions

app = FastAPI(title="Advanced Semantic Movie Search API with Re-ranking")

# 1. Initialize Models
MODEL_NAME = "all-MiniLM-L6-v2"
CROSS_ENCODER_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"

print("Loading Bi-Encoder for vector retrieval...")
bi_encoder = SentenceTransformer(MODEL_NAME)

print("Loading Cross-Encoder for contextual re-ranking...")
cross_encoder = CrossEncoder(CROSS_ENCODER_NAME)

# 2. Initialize Vector DB Client
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)
collection = chroma_client.get_collection(name="movies")

@app.get("/search")
async def search_movies(
    query: str = Query(..., description="The semantic search query"),
    limit: int = 5
):

    # --- Stage 2: Retrieve Candidates from ChromaDB ---
    # We retrieve 25 candidates so the Cross-Encoder has a healthy pool to re-rank.
    RETRIEVAL_POOL_SIZE = max(25, limit * 2)

    results = collection.query(
        query_texts=[query],
        n_results=RETRIEVAL_POOL_SIZE
    )

    # Extract candidates from ChromaDB format
    candidates = []
    if results and results['ids'] and len(results['ids'][0]) > 0:
        for i in range(len(results['ids'][0])):
            candidates.append({
                 "id": results['ids'][0][i],
                "title": results['metadatas'][0][i]['title'],
                "director": results['metadatas'][0][i]['director'],
                "release_date": results['metadatas'][0][i]['release_date'],
                "score_rating": results['metadatas'][0][i]['vote_average'], # Closer to 0 means a closer semantic match
                "bi_encoder_distance": results['distances'][0][i],
                "matched_context": results['documents'][0][i]
            })

    if not candidates:
        return {"query": query, "total_results_returned": 0, "results": []}

    # --- Stage 3: Cross-Encoder Re-ranking ---
    # Prepare pairs for the Cross-Encoder: [(Query, MovieText1), (Query, MovieText2), ...]
    cross_inputs = [[query, item["matched_context"]] for item in candidates]

    # Compute relevance scores (higher scores mean tighter semantic matching)
    re_rank_scores = cross_encoder.predict(cross_inputs)

    # Attach the new scores to our candidates
    for idx, score in enumerate(re_rank_scores):
        candidates[idx]["cross_encoder_score"] = float(score)

    # Sort candidates by the Cross-Encoder score in descending order (highest score first)
    sorted_candidates = sorted(candidates, key=lambda x: x["cross_encoder_score"], reverse=True)

    # Trim the results down to the final requested limit
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
