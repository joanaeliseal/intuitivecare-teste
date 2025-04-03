-- CRIAÇÃO DA TABELA "OPERADORAS"
CREATE TABLE operadoras (
    registro_ans INTEGER PRIMARY KEY,
    cnpj VARCHAR(20),
    razao_social TEXT,
    nome_fantasia TEXT,
    modalidade TEXT,
    logradouro TEXT,
    numero VARCHAR(10),
    complemento TEXT,
    bairro TEXT,
    cidade TEXT,
    uf CHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(5),
    telefone VARCHAR(15),
    fax VARCHAR(15),
    email TEXT,
    representante TEXT,
    cargo_representante TEXT,
    regiao_comercializacao INTEGER,
    data_registro DATE
);

-- ALTERAÇÃO DO TIPO DE COLUNA
ALTER TABLE operadoras ALTER COLUMN telefone TYPE TEXT;
ALTER TABLE operadoras ALTER COLUMN numero TYPE TEXT;

-- CRIAÇÃO DA TABELA "DEMONSTRATIVOS"
CREATE TABLE demonstrativos (
    data DATE,
    reg_ans INTEGER,
    cd_conta_contabil VARCHAR(20),
    descricao TEXT,
    vl_saldo_inicial NUMERIC,
    vl_saldo_final NUMERIC
);

-- IMPORT DOS ARQUIVOS (PELO PSQL TooL)

-- Import do operadores de plano
\copy operadoras FROM 'C:/Users/joana/OneDrive/Documentos/GITHUB/intuitivecare-teste/teste-03-banco-dados/dados/FTP-PDA-operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv' 
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'LATIN1');

SELECT * FROM operadoras LIMIT(10);

-- Import dos demonstrativos trimestrais

-- primeiro trimestre
\copy demonstrativos FROM 'C:/Users/joana/OneDrive/Documentos/GITHUB/intuitivecare-teste/teste-03-banco-dados/dados/FTP-PDA-demonstracoes_contabeis/1T2024_convertido.csv' 
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'LATIN1');

-- segundo trimestre
\copy demonstrativos FROM 'C:/Users/joana/OneDrive/Documentos/GITHUB/intuitivecare-teste/teste-03-banco-dados/dados/FTP-PDA-demonstracoes_contabeis/2T2024_convertido.csv' 
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'LATIN1');

-- terceiro trimestre
\copy demonstrativos FROM 'C:/Users/joana/OneDrive/Documentos/GITHUB/intuitivecare-teste/teste-03-banco-dados/dados/FTP-PDA-demonstracoes_contabeis/3T2024_convertido.csv' 
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'LATIN1');

-- quarto trimestre
\copy demonstrativos FROM 'C:/Users/joana/OneDrive/Documentos/GITHUB/intuitivecare-teste/teste-03-banco-dados/dados/FTP-PDA-demonstracoes_contabeis/4T2024_convertido.csv' 
WITH (FORMAT csv, HEADER true, DELIMITER ';', ENCODING 'LATIN1');

SELECT * FROM demonstrativos LIMIT(15);

-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU 
-- AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT 
    o.registro_ans,
    o.nome_fantasia,
    SUM(d.vl_saldo_final) AS total_despesas
FROM demonstrativos d
JOIN operadoras o ON o.registro_ans = d.reg_ans
WHERE d.data BETWEEN '2024-10-01' AND '2024-12-31'
  AND d.cd_conta_contabil IN ('12331101', '12331102', '12331103')
GROUP BY o.registro_ans, o.nome_fantasia
ORDER BY total_despesas DESC
LIMIT 10;

-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

SELECT 
    o.registro_ans,
    o.nome_fantasia,
    SUM(d.vl_saldo_final) AS total_despesas
FROM demonstrativos d
JOIN operadoras o ON o.registro_ans = d.reg_ans
WHERE d.data BETWEEN '2024-01-01' AND '2024-12-31'
  AND d.cd_conta_contabil IN ('12331101', '12331102', '12331103')
GROUP BY o.registro_ans, o.nome_fantasia
ORDER BY total_despesas DESC
LIMIT 10;