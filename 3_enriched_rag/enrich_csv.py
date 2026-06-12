import pandas as pd
import ollama
from tqdm import tqdm

INPUT_CSV = "movies.csv"
OUTPUT_CSV = "enriched_movies.csv"

# Point to Ollama running on your Mac's native port
local_client = ollama.Client(host="http://host.docker.internal:11434")

print(f"Loading {INPUT_CSV}...")
df = pd.read_csv(INPUT_CSV)
df_subset = df.head(100).copy() # Testing on 100 entries

enriched_profiles = []

print("Starting LOCAL AI Semantic Enrichment via Ollama (Gemma3)...")
for idx, row in tqdm(df_subset.iterrows(), total=df_subset.shape[0]):
    title = str(row.get("title", "Unknown Title"))
    overview = str(row.get("overview", ""))

    if not overview or overview == "nan":
        enriched_profiles.append("")
        continue

    prompt = f"Movie Title: {title}\nSummary: {overview}\n\nGenerate a single short paragraph describing this movie's hidden semantic themes, visual mood, and abstract search terms. Do not include headers or bullets."

    try:
        response = local_client.generate(
            model="gemma3",
            prompt=prompt,
            options={"temperature": 0.2}
        )
        enriched_profiles.append(response['response'].strip())
    except Exception as e:
        enriched_profiles.append("")

df_subset["ai_enriched_metadata"] = enriched_profiles
df_subset.to_csv(OUTPUT_CSV, index=False)
print(f"Local enrichment complete! File saved as '{OUTPUT_CSV}'")
