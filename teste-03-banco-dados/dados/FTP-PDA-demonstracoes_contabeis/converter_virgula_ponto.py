import os

# Caminho da pasta onde estão os arquivos CSV ORIGINAIS
pasta_arquivos = "C:/Users/joana/OneDrive/Documentos/GITHUB/intuitivecare-teste/teste-03-banco-dados/dados/FTP-PDA-demonstracoes_contabeis"

# Arquivos que você deseja converter
arquivos = ["1T2024.csv", "2T2024.csv", "3T2024.csv", "4T2024.csv"]

for nome_arquivo in arquivos:
    caminho_entrada = os.path.join(pasta_arquivos, nome_arquivo)
    caminho_saida = os.path.join(pasta_arquivos, nome_arquivo.replace(".csv", "_convertido.csv"))

    with open(caminho_entrada, "r", encoding="latin1") as origem, open(caminho_saida, "w", encoding="latin1") as destino:
        header = origem.readline()
        destino.write(header)  # escreve o cabeçalho

        for linha in origem:
            colunas = linha.strip().split(";")
            # Substitui vírgula por ponto nas colunas de valor (índices 4 e 5)
            if len(colunas) >= 6:
                colunas[4] = colunas[4].replace(",", ".")
                colunas[5] = colunas[5].replace(",", ".")
            nova_linha = ";".join(colunas) + "\n"
            destino.write(nova_linha)

    print(f"✅ Arquivo convertido: {caminho_saida}")
