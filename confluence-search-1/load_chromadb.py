import os
import json
import chromadb
from chromadb.utils import embedding_functions
from tqdm import tqdm

# 1. Configuration
# Change this to the path of the folder containing your JSON files
FOLDER_PATH = "./files_BCB"
MODEL_NAME = "all-MiniLM-L6-v2"

# Ensure the folder exists before running
if not os.path.exists(FOLDER_PATH):
    raise FileNotFoundError(f"The directory {FOLDER_PATH} does not exist.")

# Get a list of all JSON files in the directory
json_files = [f for f in os.listdir(FOLDER_PATH) if f.endswith('.json')]
print(f"Found {len(json_files)} JSON files in {FOLDER_PATH}...")

# 2. Setup ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)

# Changed collection name to 'open_finance' to match your new data context
collection = chroma_client.get_or_create_collection(name="open_finance", embedding_function=embedding_fn)

print("Processing files and generating text metadata profiles...")

ids = []
documents = []
metadatas = []

# Iterate through each file with a progress bar
for idx, file_name in enumerate(tqdm(json_files)):
    file_path = os.path.join(FOLDER_PATH, file_name)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {file_name}: {e}. Skipping.")
        continue

    # Extract fields based on your new schema
    texto = data.get("texto", "").strip()
    pagina_id = file_name.split(".")[0]
    title = data.get("title", "Untitled Document").strip()
    url = data.get("url", "")

    # Validation: Drop records that don't have core content or a title
    if not texto or title == "Untitled Document":
        continue

    # AI Enrichment / Semantic Profile construction
    semantic_profile = f"Title: {title}\n"
    semantic_profile += f"Content: {texto}"

    # Save data arrays (Using paginaId as the unique vector ID)
    ids.append(str(pagina_id))
    documents.append(semantic_profile)
    metadatas.append({
        "title": title,
        "pagina_id": pagina_id,
        "url": url,
        "file_name": file_name  # Useful for tracking back to the source file
    })

# 3. Batch Upload to Vector Database
BATCH_SIZE = 500
print(f"\nIndexing {len(documents)} documents into ChromaDB in batches of {BATCH_SIZE}...")

for i in range(0, len(ids), BATCH_SIZE):
    end_idx = min(i + BATCH_SIZE, len(ids))
    collection.add(
        ids=ids[i:end_idx],
        documents=documents[i:end_idx],
        metadatas=metadatas[i:end_idx]
    )
    print(f"Indexed records {i} to {end_idx}...")

print(f"\nSuccessfully built your database! Total vectors in collection: {collection.count()}")
