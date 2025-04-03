# 🧪 Teste Técnico - IntuitiveCare (Estágio)

Este repositório contém a minha participação no teste técnico proposto pela IntuitiveCare, referente ao processo seletivo para a vaga de estágio. A proposta consiste em resolver 4 desafios técnicos em até 7 dias (de 28/03 a 04/04).

## 📋 Estrutura dos Testes

### ✅ Teste 1 - Web Scraping
- [x] Acessar o site da ANS
- [x] Fazer o download dos arquivos PDF (Anexos I e II)
- [x] Compactar os arquivos em `.zip`

### ✅ Teste 2 - Transformação de Dados
- [x] Extrair dados da tabela do Anexo I (PDF)
- [x] Converter os dados em um arquivo `.csv`
- [x] Substituir abreviações OD e AMB por seus significados completos
- [x] Compactar em `Teste_{meu_nome}.zip`

### ✅ Teste 3 - Banco de Dados
- [x] Baixar os arquivos da ANS (dados contábeis e operadoras)
- [x] Criar tabelas no PostgreSQL
- [x] Importar os dados com encoding correto
- [x] Realizar queries analíticas

### ⚙️ Teste 4 - API com Interface Web
- [x] Criar backend em Python (Flask)
- [x] Criar rota de busca textual no CSV de operadoras
- [x] Integrar com frontend em Vue.js
- [x] Criar coleção Postman para testes

---

## 🚀 Tecnologias Utilizadas

| Etapa | Linguagem/Framework | Observação |
|-------|----------------------|------------|
| Web Scraping | Python (`requests`, `BeautifulSoup`) | Também usei `zipfile` para compactação |
| Transformação de Dados | Python (`pdfplumber`, `pandas`) | PDFs complexos exigem bibliotecas |
| Banco de Dados | PostgreSQL 15 | Utilizado via `pgAdmin 4` |
| API | Python (`FastAPI`) | Backend simples |
| Interface | Vue.js (CLI) | Integração com a API |
| Testes de rota | Postman | Documentação e testes |

---

## 💡 Aprendizados e Desafios

Este desafio técnico foi uma excelente oportunidade de aprender na prática sobre:
- Web scraping de sites públicos
- Manipulação de PDFs e transformação de dados
- Construção de queries SQL com foco em análise de dados
- Desenvolvimento de uma API REST e integração com frontend Vue.js

Alguns testes estão parcialmente implementados devido à curva de aprendizado, mas todos os passos foram documentados e comentados no código.

---

## 📁 Organização do Repositório
```
📦 intuitivecare-teste
├── teste-01-webscraping
├── teste-02-transformacao-dados
├── teste-03-banco-dados
├── teste-04-api-interface
├── README.md
```

---

## ✍️ Contato
Caso deseje conversar sobre este projeto ou tenha interesse em ver meu progresso, fico à disposição:
- **Nome:** [Seu Nome Aqui]
- **LinkedIn:** [Seu LinkedIn]
- **E-mail:** [Seu E-mail]

---

> _"Aprender fazendo é a melhor forma de evoluir na área de tecnologia. Obrigada pela oportunidade!"_
