import json
import math
import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from tqdm import tqdm

# 1. Configuration
PARQUET_FILE_PATH = "file.parquet"  # <-- Your Parquet data source
MODEL_NAME = "all-MiniLM-L6-v2"

print(f"Reading columnar format from {PARQUET_FILE_PATH}...")
# Pandas handles Parquet files natively using the pyarrow engine
df = pd.read_parquet(PARQUET_FILE_PATH)

# 2. Setup ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_storage")
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=MODEL_NAME)
collection = chroma_client.get_or_create_collection(name="enriched_api_logs", embedding_function=embedding_fn)

print("Parsing structural properties and extracting nested payloads...")

ids = []
documents = []
metadatas = []

for idx, row in tqdm(df.iterrows(), total=df.shape[0]):
    # Extract structural unique identifier
    trace_id = str(row.get("trace_id", idx))
    print(f"\nProcessing trace_id: {trace_id} (Row {idx + 1}/{df.shape[0]})")

    # --- HANDLING COLUMNS/OBJECTS SAFELY ---
    # Parquet files might read nested structures as dictionaries natively, or as stringified JSON strings.
    # This helper forces a safe dictionary conversion regardless of format.
    def get_dict_property(field_data):
        if pd.isna(field_data) or field_data is None:
            return {}
        if isinstance(field_data, dict):
            return field_data
        try:
            return json.loads(str(field_data))
        except:
            return {}

    http_obj = get_dict_property(row.get("http"))
    sensedia_obj = get_dict_property(row.get("sensedia"))

    # Extract primary query parameters
    method = str(http_obj.get("method", "UNKNOWN"))
    url = str(http_obj.get("url", "UNKNOWN"))
    status_code = http_obj.get("status_code", 0)

    # Extract inner trace workflows
    trace_data = sensedia_obj.get("trace", "[]")
    semantic_messages = []
    try:
        # Check if the trace field inside sensedia object is still a string
        trace_array = json.loads(trace_data) if isinstance(trace_data, str) else trace_data
        if isinstance(trace_array, list):
            for t_item in trace_array:
                if isinstance(t_item, dict) and "message" in t_item:
                    semantic_messages.append(t_item["message"])
    except Exception:
        pass

    # --- DYNAMIC ADDITIONAL_INFO UNPACKING ---
    add_info = sensedia_obj.get("additional_info", [])
    if isinstance(add_info, str):
        try: add_info = json.loads(add_info)
        except: add_info = []

    additional_info_narrative = []
    flattened_metadata = {}

    if isinstance(add_info, list):
        for item in add_info:
            if isinstance(item, dict):
                key = item.get("key")
                val = item.get("value")
                if key:
                    if isinstance(val, (str, int, float, bool)):
                        flattened_metadata[f"info_{key}"] = val
                        additional_info_narrative.append(f"Property {key} is set to {val}.")
                    elif isinstance(val, dict):
                        flattened_metadata[f"info_{key}"] = json.dumps(val)
                        sub_properties = ", ".join([f"{k}: {v}" for k, v in val.items()])
                        additional_info_narrative.append(f"Property {key} contains metrics ({sub_properties}).")

    # --- NARRATIVE COMPOSITION (THE VECTOR DOCUMENT) ---
    document_text = (
        f"HTTP {method} transaction processed at {url}. "
        f"Response status: {status_code}. "
        f"Workflow Execution Trace: {' -> '.join(semantic_messages)}. "
        f"Dynamic Parameters Context: {' '.join(additional_info_narrative)}"
    )

    # --- STRUCTURAL FILTER BASE MAP (THE METADATA) ---
    app_data = sensedia_obj.get("app", {})
    env_data = sensedia_obj.get("environment", {})

    metadata_payload = {
        "url": url,
        "method": method,
        "status_code": int(status_code) if not math.isnan(status_code) else 0,
        "app_name": app_data.get("name", "Unknown App") if isinstance(app_data, dict) else "Unknown App",
        "environment": env_data.get("name", "Unknown Env") if isinstance(env_data, dict) else "Unknown Env",
        **flattened_metadata
    }

    # Save data arrays
    ids.append(trace_id)
    documents.append(document_text)
    metadatas.append(metadata_payload)

# 3. Batch Ingestion Engine
BATCH_SIZE = 500
print(f"\nIndexing {len(documents)} system traces into ChromaDB...")
for i in range(0, len(ids), BATCH_SIZE):
    end_idx = min(i + BATCH_SIZE, len(ids))
    collection.add(
        ids=ids[i:end_idx],
        documents=documents[i:end_idx],
        metadatas=metadatas[i:end_idx]
    )

print(f"\nDone! Database built with columnar data inputs. Vectors active: {collection.count()}")
