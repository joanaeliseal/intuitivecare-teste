import pdfplumber
import pandas as pd
import os
import zipfile

# Nomes dos arquivos de saída
base_dir = os.path.dirname(__file__)
output_csv = os.path.join(base_dir, "tabela_transformada.csv")
output_zip = os.path.join(base_dir, "Teste_Joana_Elise.zip")


def extrair_tabela_anexo1():
    """
    Lê o PDF do Anexo I e extrai todas as tabelas.
    Retorna um DataFrame com os dados estruturados.
    """
    # Caminho absoluto para a pasta de PDFs
    pdf_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../teste-01-webscraping/pdfs"))

    try:
        arquivos = os.listdir(pdf_dir)
    except FileNotFoundError:
        print("Pasta com PDFs não encontrada.")
        return None

    # Procurar arquivo que contenha "Anexo-I" ou "Anexo_I"
    anexo1 = [arq for arq in arquivos if "Anexo-I" in arq or "Anexo_I" in arq]
    if not anexo1:
        print("Arquivo Anexo I não encontrado.")
        return None

    caminho_pdf = os.path.join(pdf_dir, anexo1[0])
    tabela_total = []

    with pdfplumber.open(caminho_pdf) as pdf:
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables()
            for tabela in tabelas:
                if tabela:  # ignora páginas sem tabela
                    for linha in tabela:
                        tabela_total.append(linha)

    if not tabela_total:
        print("Nenhuma tabela encontrada no PDF.")
        return None

    colunas = tabela_total[0]
    linhas = tabela_total[1:]
    df = pd.DataFrame(linhas, columns=colunas)
    return df

def transformar_dados(df):
    """
    Substitui as abreviações OD e AMB por descrições completas.
    """
    df.replace({"OD": "Odontológico", "AMB": "Ambulatorial"}, inplace=True)
    return df

def salvar_csv(df):
    """
    Salva o DataFrame em um arquivo CSV.
    """
    df.to_csv(output_csv, index=False)
    print(f"CSV salvo como {output_csv}")

def compactar_csv():
    """
    Compacta o CSV gerado em um arquivo .zip.
    """
    with zipfile.ZipFile(output_zip, "w") as zipf:
        zipf.write(output_csv)
    print(f"Arquivo compactado como {output_zip}")

if __name__ == "__main__":
    tabela = extrair_tabela_anexo1()
    if tabela is not None:
        tabela = transformar_dados(tabela)
        salvar_csv(tabela)
        compactar_csv()
