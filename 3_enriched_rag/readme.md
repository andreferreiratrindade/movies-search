Step 1: Install Ollama on your Mac
Open your native macOS terminal (outside the container) and install Ollama via Homebrew, or download it manually:

Bash
brew install ollama
Start the background server:

Bash
ollama serve
Step 2: Pull the Required Local Models
Open a terminal window on your Mac and download the models you need:

Bash
# 1. Pull the text-generation model for metadata enrichment
ollama pull gemma3

# 2. Pull the vector embedding model for ChromaDB
ollama pull nomic-embed-text


python enrich_csv.py
python load_csv.py
python app.py
