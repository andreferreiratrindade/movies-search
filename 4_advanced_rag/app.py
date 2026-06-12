from fastapi import FastAPI, Query
from sentence_transformers import SentenceTransformer, CrossEncoder
import chromadb
from chromadb.utils import embedding_functions
import ollama

app = FastAPI(title="ChromaDB-Centric Semantic Movie Search API")

# 1. Initialize Local Ollama Client ONLY for Query Expansion text
print("Connecting to local Ollama gateway for text generation...")
local_llm_client = ollama.Client(host="http://host.docker.internal:11434")


MODEL_NAME = "all-MiniLM-L6-v2"
CROSS_ENCODER_NAME = "cross-encoder/ms-marco-MiniLM-L-6-v2"
cross_encoder = CrossEncoder(CROSS_ENCODER_NAME)

print("Loading Cross-Encoder for contextual re-ranking...")
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)
collection = chroma_client.get_collection(name="movies")

@app.get("/search")
async def search_movies(
    query: str = Query(..., description="The messy user search query"),
    limit: int = 5,
    expand_query: bool = Query(True, description="Toggle AI query expansion rewriting")
):
    final_search_text = query

    # --- Stage 1: AI Query Expansion Gateway (Ollama Gemma3) ---
    if expand_query:
        expansion_prompt = f"""
        You are an advanced search gateway optimizer for a movie search engine.
        Your task is to rewrite the user's brief or vague search query into an optimized, keyword-rich semantic description.
        Expand it using cinematic themes, alternative terms, tones, tropes, and stylistic moods.

        Original User Query: "{query}"

        Instructions:
        - Output ONLY the expanded description paragraph.
        - Do not include conversational text, headers, quotes, or preambles.
        - Keep the output under 3 sentences.
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
            final_search_text = query

    # --- Stage 2: Retrieve Candidates (ChromaDB Vector Math) ---
    RETRIEVAL_POOL_SIZE = max(25, limit * 2)

    # ChromaDB processes the local vector calculation inside your container now!
    results = collection.query(
        query_texts=[final_search_text],
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
                "score_rating": results['metadatas'][0][i]['vote_average'],
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
        "original_query": query,
        "ai_expanded_query": final_search_text if expand_query else "Expansion Disabled",
        "total_candidates_evaluated": len(candidates),
        "results_returned": len(final_results),
        "results": final_results
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
