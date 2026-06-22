import json
import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup

# Create output folder if it doesn't exist
os.makedirs("files", exist_ok=True)

HOST_OLLAMA_URL = "http://host.docker.internal:11434"
MAX_PAGINAS = 10000
MAX_CONCURRENT_REQUESTS = 10  # Limits simultaneous hits to avoid getting blocked

def save_to_json(data, filename):
    """Saves data to a JSON file synchronously (fast enough for single items)."""
    # Clean filename to avoid path traversal or illegal characters
    safe_filename = "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '_', '-')]).rstrip()
    filepath = os.path.join("files", f"{safe_filename}.json")
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Successfully saved data to '{filepath}'")
    except Exception as e:
        print(f"An error occurred while saving {filename}: {e}")

async def processar_pagina(session, url_atual, url_base, paginas_visitadas, paginas_para_visitar, documentos_finais, sem):
    """Fetches, parses, and processes a single page asynchronously."""
    if url_atual in paginas_visitadas:
        return

    paginas_visitadas.add(url_atual)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    # Generate unique ID based on URL
    url_parts = url_atual.split("/")
    paginaId = f"{url_parts[-2]}_{url_parts[-1]}"

    # Acquire semaphore slot to limit concurrency
    async with sem:
        try:
            async with session.get(url_atual, headers=headers, timeout=10) as resposta:
                if resposta.status != 200:
                    return
                html_text = await resposta.text()
        except Exception:
            return

    # Parsing HTML is CPU-bound, but for simple tasks, doing it here is fast enough
    soup = BeautifulSoup(html_text, 'html.parser')

    # 1. Content Extraction
    conteudo = soup.find(id="main-content") or soup.find(class_="wiki-content")
    if conteudo:
        titulo = soup.find("title").text.strip() if soup.find("title") else url_atual

        # --- BUG FIX & FILTER ---
        # Fixed `.contains()` bug to correct Python syntax (`in`)
        if "Histórico de Especificações" in titulo or "Changelog" in titulo:
            print(f"Sub-página pulada pelo filtro de título: {titulo}")
            return

        texto_limpo = conteudo.get_text(separator="\n", strip=True)

        if not texto_limpo.strip():
            return

        doc = paginaId


        save_to_json({"texto": texto_limpo, "paginaId": paginaId, "title": titulo, "url": url_atual}, paginaId)
        documentos_finais.append(doc)
        print(f"📥 [{len(documentos_finais)}] Coletado: {titulo}")

    # 2. Discovering links
    for link in soup.find_all("a", href=True):
        href = link["href"]
        completo_url = url_base + href
        if href.startswith("/wiki/spaces/OF/") and completo_url not in paginas_visitadas:
            if completo_url not in paginas_para_visitar:
                paginas_para_visitar.add(completo_url)

async def rastrear_e_extrair_espaco_async():
    url_base = "https://openfinancebrasil.atlassian.net"
    url_inicial = f"{url_base}/wiki/spaces/OF/overview"

    # Use a set for `paginas_para_visitar` to make checking duplicates O(1)
    paginas_para_visitar = {url_inicial}
    paginas_visitadas = set()
    documentos_finais = []

    # Semaphore protects you from overwhelming the server or getting rate-limited (HTTP 429)
    sem = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    print("🛰️ Iniciando mapeamento assíncrono do espaço público 'OF'...")

    async with aiohttp.ClientSession() as session:
        # Loop until no more pages are left or max limit reached
        while paginas_para_visitar and len(paginas_visitadas) < MAX_PAGINAS:
            # Take a batch of URLs currently ready to process
            batch = list(paginas_para_visitar)[:MAX_CONCURRENT_REQUESTS]

            # Remove them from the pending set
            for url in batch:
                paginas_para_visitar.remove(url)

            # Fire off the entire batch concurrently
            tasks = [
                processar_pagina(session, url, url_base, paginas_visitadas, paginas_para_visitar, documentos_finais, sem)
                for url in batch if url not in paginas_visitadas
            ]

            if tasks:
                await asyncio.gather(*tasks)

    return documentos_finais

def executar_pipeline():
    # Run the async crawler inside the synchronous pipeline entry point
    documentos = asyncio.run(rastrear_e_extrair_espaco_async())

    if not documentos:
        print("❌ Falha crítica: Nenhuma página encontrada.")
        return

    print(f"🎉 Finalizado! {len(documentos)} documentos processados com sucesso.")

if __name__ == "__main__":
    executar_pipeline()
