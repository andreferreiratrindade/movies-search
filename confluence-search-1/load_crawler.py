import json
from operator import contains
import os
import asyncio
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import uuid
# Cria a pasta de saída se não existir
os.makedirs("files", exist_ok=True)

# Configurações de limite do Crawler
MAX_PAGINAS = 10000
MAX_CONCURRENT_REQUESTS = 10 # Mantido baixo para evitar sobrecarga de RAM e bloqueio por IP

# Domínios permitidos (limpamos para conter apenas os domínios base)
ALLOWED_DOMAINS = {"https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu",
                    "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Circular",
                    "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Instru",
                    "https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Comunicado"}

def save_to_json(data, filename):
    """Salva os dados extraídos em um arquivo JSON de forma limpa."""
    safe_filename = "".join([c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '_', '-')]).rstrip()
    if not safe_filename:
        safe_filename = "documento_sem_nome"

    # Limita o tamanho do nome do arquivo para evitar erros de sistema operacional
    filepath = os.path.join("files_BCB", f"{uuid.uuid4()}.json")
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"✅ Arquivo salvo: '{filepath}'")
    except Exception as e:
        print(f"❌ Erro ao salvar {filename}: {e}")

async def processar_pagina(context, url_atual, paginas_visitadas, paginas_para_visitar, documentos_finais, sem):
    """Abre um navegador invisível, renderiza o JS e extrai os dados."""
    if url_atual in paginas_visitadas:
        return

    paginas_visitadas.add(url_atual)

    # Gera um ID único baseado na URL para o nome do arquivo JSON
    url_parsed = urlparse(url_atual)
    url_path = url_parsed.path.strip("/")
    prefixo = url_parsed.netloc.replace(".", "_")
    paginaId = f"{prefixo}_{url_path.replace('/', '_')}" if url_path else f"{prefixo}_home"

    async with sem:
        page = await context.new_page()
        try:
            # Delay anti-bloqueio essencial
            await asyncio.sleep(0.6)

            # networkidle: aguarda até que não haja conexões de rede por pelo menos 500ms (perfeito para SPAs)
            resposta = await page.goto(url_atual, wait_until="networkidle", timeout=25000)

            if resposta and resposta.status >= 400:
                print(f"⚠️ Falha de acesso [{resposta.status}]: {url_atual}")
                return

            # Para garantir que o Angular do BCB teve tempo de renderizar a DOM após o download da rede
            if "bcb.gov.br" in url_atual:
                await page.wait_for_timeout(2000)

            # Extrai o HTML renderizado (pós-JavaScript)
            html_text = await page.content()

        except PlaywrightTimeoutError:
            print(f"⏳ Timeout ignorado: {url_atual}")
            return
        except Exception as e:
            return
        finally:
            # É crucial fechar a página para não estourar a memória RAM
            await page.close()

    soup = BeautifulSoup(html_text, 'html.parser')

    # Estruturas comuns de conteúdo
    conteudo = soup.find('main') or soup.find('article') or soup.find(id='content') or soup.find(class_='site-content') or soup.find('body')

    if conteudo:
        titulo = soup.find("title").text.strip() if soup.find("title") else url_atual
        titulo = titulo.split("|")[0].split("-")[0].strip()

        # Remove elementos que poluem o corpo do texto regulatório
        for ignore_tag in conteudo(["script", "style", "nav", "footer", "header", "form"]):
            ignore_tag.extract()

        texto_limpo = conteudo.get_text(separator="\n", strip=True)

        if len(texto_limpo) > 150:  # Garante que a página possui conteúdo útil relevante
            save_to_json({"texto": texto_limpo, "paginaId": paginaId, "title": titulo, "url": url_atual}, paginaId)
            documentos_finais.append(paginaId)
            print(f"📥 [{len(documentos_finais)}] Coletado com sucesso: {url_atual}")

    # --- DESCOBERTA E RASTREAMENTO DE LINKS INTERLIGADOS ---
    for link in soup.find_all("a", href=True):
        href = link["href"]
        completo_url = urljoin(url_atual, href)
        parsed_url = urlparse(completo_url)

        # Validações de segurança básicas para o Crawler
        is_allowed_domain = completo_url.startswith(tuple(ALLOWED_DOMAINS))
        is_not_anchor = not href.startswith("#")
        is_not_file = not parsed_url.path.lower().endswith(('.pdf', '.zip', '.docx', '.xlsx', '.png', '.jpg', '.mp3', '.mp4'))

        if is_allowed_domain and is_not_anchor and is_not_file:
            path_lower = parsed_url.path.lower()

            # Condição 1: Se for Open Finance, foca prioritariamente em atos-normativos
            is_of_target = "openfinancebrasil.org.br" in parsed_url.netloc and "/atos-normativos" in path_lower

            # Condição 2: Se for BCB, aceita qualquer ramificação interna encontrada
            is_bcb_target = "bcb.gov.br" in parsed_url.netloc

            if is_of_target or is_bcb_target:
                if completo_url not in paginas_visitadas and completo_url not in paginas_para_visitar:
                    paginas_para_visitar.add(completo_url)

async def iniciar_crawler_async():
    url_inicial = "https://openfinancebrasil.org.br/atos-normativos/"

    paginas_para_visitar = {url_inicial.rstrip("/")}
    paginas_visitadas = set()
    documentos_finais = []

    sem = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    print("🛰️ Rastreando Open Finance e BCB usando Headless Browser (Playwright)...")

    # Inicia o Playwright e o navegador Chromium
    async with async_playwright() as p:
        # headless=True roda invisível em background. Mude para False se quiser ver a "mágica" acontecer.
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            locale="pt-BR"
        )

        while paginas_para_visitar and len(paginas_visitadas) < MAX_PAGINAS:
            batch = list(paginas_para_visitar)[:MAX_CONCURRENT_REQUESTS]

            for url in batch:
                paginas_para_visitar.remove(url)

            tasks = [
                processar_pagina(context, url, paginas_visitadas, paginas_para_visitar, documentos_finais, sem)
                for url in batch if url not in paginas_visitadas
            ]

            if tasks:
                await asyncio.gather(*tasks)

        await browser.close()

    return documentos_finais

def executar_pipeline():
    documentos = asyncio.run(iniciar_crawler_async())

    if not documentos:
        print("❌ Fim da execução: Nenhuma página válida pôde ser extraída.")
        return

    print(f"🎉 Rastreamento concluído! {len(documentos)} arquivos JSON salvos na pasta 'files'.")

if __name__ == "__main__":
    executar_pipeline()
