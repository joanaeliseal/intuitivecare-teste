import requests
import os
import zipfile

# Diretório onde os PDFs serão salvos
output_dir = os.path.join(os.path.dirname(__file__), "pdfs")

# Acessar os links dos Anexos I e II
pdf_urls = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

def baixar_pdfs():
    """
    Baixa os arquivos PDF dos links definidos e os salva na pasta 'pdfs' local ao script.
    Etapas:
    - Cria a pasta 'pdfs' se ela ainda não existir.
    - Para cada link na lista, faz o download do conteúdo.
    - Salva o arquivo com o nome original extraído da URL.
    """

    output_dir = os.path.join(os.path.dirname(__file__), "pdfs")
    os.makedirs(output_dir, exist_ok=True)

    for url in pdf_urls:
        nome_arquivo = url.split("/")[-1]
        caminho = os.path.join(output_dir, nome_arquivo)
        print(f"Baixando {nome_arquivo}...")
        response = requests.get(url)
        with open(caminho, "wb") as f:
            f.write(response.content)

def compactar_pdfs():
    """
    Compacta todos os arquivos da pasta 'pdfs' em um único arquivo chamado 'anexos.zip'.
    Etapas:
    - Cria um arquivo .zip chamado 'anexos.zip'.
    - Adiciona todos os arquivos da pasta 'pdfs' ao zip.
    - Mantém apenas o nome dos arquivos dentro do zip (sem o caminho).
    """
    with zipfile.ZipFile("anexos.zip", "w") as zipf:
        for file in os.listdir(output_dir):
            zipf.write(os.path.join(output_dir, file), arcname=file)

    print("Arquivos compactados em anexos.zip")

if __name__ == "__main__":
    baixar_pdfs()
    compactar_pdfs()
