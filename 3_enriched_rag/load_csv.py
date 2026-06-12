import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from tqdm import tqdm
import math

# 1. Configuration
CSV_FILE_PATH = "enriched_movies.csv"  # <-- Change this to your actual filename
MODEL_NAME = "all-MiniLM-L6-v2"

print(f"Reading {CSV_FILE_PATH}...")
# Read the CSV file, ensuring IDs are read as strings
df = pd.read_csv(CSV_FILE_PATH, dtype={"id": str})

# 2. Setup ChromaDB client (Persisted to a local folder so data stays saved)
# This saves the data to a folder called 'chroma_storage' in your workspace
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)
collection = chroma_client.get_or_create_collection(name="movies", embedding_function=embedding_fn)

print("Processing movies and generating text metadata profiles...")

ids = []
documents = []
metadatas = []

for idx, row in tqdm(df.iterrows(), total=df.shape[0]):
    # Extract structural identifiers
    movie_id = str(row.get("id", idx))
    title = str(row.get("title", row.get("original_title", "Unknown Title")))

    # Extract narrative and thematic elements
    overview = str(row.get("overview", "")) if pd.notna(row.get("overview")) else ""
    tagline = str(row.get("tagline", "")) if pd.notna(row.get("tagline")) else ""
    keywords = str(row.get("keywords", "")) if pd.notna(row.get("keywords")) else ""
    genres = str(row.get("genres", "")) if pd.notna(row.get("genres")) else ""
    director = str(row.get("director", "")) if pd.notna(row.get("director")) else ""

    # Drop rows that don't have a plot summary or title
    if not overview or title == "Unknown Title":
        continue

    # AI Enrichment: Combine multiple features to give the vectorizer deep context.
    # We include genres, tagline, keywords, and director alongside the main overview.
    semantic_profile = f"Title: {title}. "
    if tagline:
         semantic_profile += f"Tagline: {tagline}. "
    semantic_profile += f"Overview: {overview} "
    if keywords:
         semantic_profile += f"Keywords: {keywords}. "
    if genres:
         semantic_profile += f"Genres: {genres}. "
    if director and director != "nan":
         semantic_profile += f"Directed by: {director}."

    # Prevent floating point errors in numeric metadata values
    vote_avg = row.get("vote_average", 0.0)
    vote_avg = 0.0 if math.isnan(vote_avg) else float(vote_avg)

    release_date = str(row.get("release_date", "Unknown"))
    if pd.isna(row.get("release_date")):
        release_date = "Unknown"

    # Save data arrays
    ids.append(movie_id)
    documents.append(semantic_profile)
    metadatas.append({
        "title": title,
        "director": director if director != "nan" else "Unknown",
        "release_date": release_date,
        "vote_average": vote_avg
    })

# 3. Batch Upload to Vector Database
# ChromaDB works best when adding records in chunks (batches)
BATCH_SIZE = 500
print(f"\nIndexing {len(documents)} movies into ChromaDB in batches of {BATCH_SIZE}...")

for i in range(0, len(ids), BATCH_SIZE):
    end_idx = min(i + BATCH_SIZE, len(ids))
    collection.add(
        ids=ids[i:end_idx],
        documents=documents[i:end_idx],
        metadatas=metadatas[i:end_idx]
    )
    print(f"Indexed records {i} to {end_idx}...")

print(f"\nSuccessfully built your database! Total vectors in collection: {collection.count()}")
