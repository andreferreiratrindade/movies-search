import json
from pathlib import Path


def sanitize_filename(filename):
    """Remove caracteres inválidos para nomes de arquivos."""
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, "")
    return filename


def convert_json_folder_to_md(input_folder, output_folder):
    """Lê todos os JSONs de uma pasta e os converte para Markdown (.md) otimizado

    para IA.
    """
    in_dir = Path(input_folder)
    out_dir = Path(output_folder)

    # Cria a pasta de saída se ela não existir
    out_dir.mkdir(parents=True, exist_ok=True)

    if not in_dir.exists() or not in_dir.is_dir():
        print(f"Erro: A pasta de entrada '{input_folder}' não existe.")
        return

    # Busca todos os arquivos .json na pasta
    json_files = list(in_dir.glob("*.json"))

    if not json_files:
        print(f"Nenhum arquivo JSON encontrado em '{input_folder}'.")
        return

    print(
        f"Encontrados {len(json_files)} arquivos JSON. Iniciando conversão..."
    )

    for file_path in json_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Extrai os dados do seu padrão JSON
            texto = data.get("texto", "")
            pagina_id = data.get("paginaId", "sem_id")
            title = data.get("title", "Sem Título")
            url = data.get("url", "")

            # Define o nome do arquivo .md baseado no title ou paginaId
            safe_title = sanitize_filename(title[:50])  # Limita o tamanho
            md_filename = f"{pagina_id}_{safe_title}.md"
            md_file_path = out_dir / md_filename

            # Estrutura o conteúdo do Markdown otimizado para IA (RAG / Embeddings)
            md_content = f"""---
                            title: "{title}"
                            paginaId: "{pagina_id}"
                            url: "{url}"
                            source: "Open Finance Brasil Confluence"
                            ---

                            # {title}

                            {texto}
"""

            # Salva o arquivo Markdown
            with open(md_file_path, "w", encoding="utf-8") as f_md:
                f_md.write(md_content)

            print(f"Convertido com sucesso: {md_filename}")

        except json.JSONDecodeError:
            print(f"Erro de sintaxe JSON no arquivo: {file_path.name}")
        except Exception as e:
            print(f"Erro ao processar {file_path.name}: {e}")


# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Configure aqui os caminhos das suas pastas
    pasta_dos_jsons = "./files"
    pasta_de_saida_md = "./arquivos_markdown"



    # Executa a conversão
    convert_json_folder_to_md(pasta_dos_jsons, pasta_de_saida_md)
