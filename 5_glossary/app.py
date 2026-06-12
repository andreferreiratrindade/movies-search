from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional
from sentence_transformers import SentenceTransformer, CrossEncoder
import chromadb
from chromadb.utils import embedding_functions

app = FastAPI(title="Glossary-Enhanced Movie Search API with Management Controls")

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

movie_collection = chroma_client.get_collection(name="movies")
glossary_collection = chroma_client.get_collection(name="glossary")


# 3. Pydantic Data Models for Request Validation
class MovieModel(BaseModel):
    id: str = Field(..., description="Unique alphanumeric identifier for the movie")
    title: str = Field(..., description="Official title of the movie")
    overview: str = Field(..., description="Plot summary or synopsis")
    tagline: Optional[str] = ""
    keywords: Optional[str] = ""
    genres: Optional[str] = ""
    director: Optional[str] = "Unknown"
    vote_average: Optional[float] = 0.0
    release_date: Optional[str] = "Unknown"


class MovieUpdateModel(BaseModel):
    title: Optional[str] = None
    overview: Optional[str] = None
    tagline: Optional[str] = None
    keywords: Optional[str] = None
    genres: Optional[str] = None
    director: Optional[str] = None
    vote_average: Optional[float] = None
    release_date: Optional[str] = None


# Helper function to generate uniform semantic context vectors match your load_csv structure
def build_semantic_profile(movie: dict) -> str:
    profile = f"Title: {movie.get('title')}. "
    if movie.get("tagline"):
         profile += f"Tagline: {movie.get('tagline')}. "

    profile += f"Overview: {movie.get('overview')} "

    if movie.get("keywords"):
         profile += f"Keywords: {movie.get('keywords')}. "
    if movie.get("genres"):
         profile += f"Genres: {movie.get('genres')}. "
    if movie.get("director") and movie.get("director") != "nan":
         profile += f"Directed by: {movie.get('director')}."
    return profile


# --- READ: Existing Search Engine Endpoint ---
@app.get("/search")
async def search_movies(
    query: str = Query(..., description="The semantic search query"),
    limit: int = 5
):
    glossary_results = glossary_collection.query(query_texts=[query], n_results=1)
    refined_query = query
    glossary_context_added = None

    if glossary_results and glossary_results['ids'] and len(glossary_results['ids'][0]) > 0:
        if glossary_results['distances'][0][0] < 1.0:
            matched_term = glossary_results['metadatas'][0][0]['term']
            refined_query = f"{query} {matched_term}"
            glossary_context_added = f"Matched internal glossary term: '{matched_term}'"

    RETRIEVAL_POOL_SIZE = max(25, limit * 2)
    results = movie_collection.query(query_texts=[refined_query], n_results=RETRIEVAL_POOL_SIZE)

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

    cross_inputs = [[refined_query, item["matched_context"]] for item in candidates]
    re_rank_scores = cross_encoder.predict(cross_inputs)

    for idx, score in enumerate(re_rank_scores):
        candidates[idx]["cross_encoder_score"] = float(score)

    sorted_candidates = sorted(candidates, key=lambda x: x["cross_encoder_score"], reverse=True)
    final_results = sorted_candidates[:limit]

    return {
        "original_query": query,
        "internal_expansion": glossary_context_added,
        "results": final_results
    }


# --- CREATE: Add a New Movie ---
@app.post("/movies", status_code=status.HTTP_201_CREATED)
async def add_movie(movie: MovieModel):
    # Check if ID already exists to prevent silent overwrites
    existing = movie_collection.get(ids=[movie.id])
    if existing and existing['ids']:
        raise HTTPException(
            status_code=400,
            detail=f"Movie with ID '{movie.id}' already exists. Use PUT endpoint to update it."
        )

    # Process attributes and generate the core embedding content text
    movie_dict = movie.model_dump()
    document_text = build_semantic_profile(movie_dict)

    # Isolate traditional metadata fields
    metadata = {
        "title": movie.title,
        "director": movie.director,
        "release_date": movie.release_date,
        "vote_average": movie.vote_average
    }

    # Write directly to ChromaDB (it automatically calculates vector embeddings using embedding_fn)
    movie_collection.add(
        ids=[movie.id],
        documents=[document_text],
        metadatas=[metadata]
    )

    return {"message": "Movie successfully added and indexed", "movie_id": movie.id}


# --- UPDATE: Modify details of an Existing Movie ---
@app.put("/movies/{movie_id}")
async def update_movie(movie_id: str, update_data: MovieUpdateModel):
    # Step 1: Verify the record exists and extract current values
    existing = movie_collection.get(ids=[movie_id])
    if not existing or not existing['ids']:
        raise HTTPException(
            status_code=404,
            detail=f"Movie with ID '{movie_id}' not found."
        )

    # Reconstruct original fields out of existing metadata and content strings
    current_metadata = existing['metadatas'][0]
    current_document = existing['documents'][0]

    # Extract back features not directly stored explicitly in metadata flat fields
    # If explicit extraction fails, fallback gracefully or use patch data
    provided_updates = update_data.model_dump(exclude_unset=True)

    # Re-build target record using old state layered under new patched changes
    updated_movie_state = {
        "title": provided_updates.get("title", current_metadata.get("title")),
        "director": provided_updates.get("director", current_metadata.get("director")),
        "release_date": provided_updates.get("release_date", current_metadata.get("release_date")),
        "vote_average": provided_updates.get("vote_average", current_metadata.get("vote_average")),
        "overview": provided_updates.get("overview", current_document), # Base fallback
        "tagline": provided_updates.get("tagline", ""),
        "keywords": provided_updates.get("keywords", ""),
        "genres": provided_updates.get("genres", "")
    }

    # Recalculate context document profile if core semantic parameters changed
    new_document_text = build_semantic_profile(updated_movie_state)

    new_metadata = {
        "title": updated_movie_state["title"],
        "director": updated_movie_state["director"],
        "release_date": updated_movie_state["release_date"],
        "vote_average": updated_movie_state["vote_average"]
    }

    # Commit modifications using update element structure
    movie_collection.update(
        ids=[movie_id],
        documents=[new_document_text],
        metadatas=[new_metadata]
    )

    return {"message": "Movie successfully updated and re-indexed", "movie_id": movie_id}


# --- DELETE: Remove a Movie ---
@app.delete("/movies/{movie_id}")
async def delete_movie(movie_id: str):
    # Verify the record exists before removing
    existing = movie_collection.get(ids=[movie_id])
    if not existing or not existing['ids']:
        raise HTTPException(
            status_code=404,
            detail=f"Movie with ID '{movie_id}' not found."
        )

    movie_collection.delete(ids=[movie_id])
    return {"message": f"Movie with ID '{movie_id}' was deleted successfully."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
