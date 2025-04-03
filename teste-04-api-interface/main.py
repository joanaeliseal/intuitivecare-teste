# Criando um servidor web com Python usando FastAPI, 
# que expõe uma API REST para buscar dados de um CSV.

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Libera acesso para o frontend (Vue.js)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega o CSV na inicialização
df = pd.read_csv("dados/Relatorio_cadop.csv", sep=";", encoding="latin1")

@app.get("/")
def root():
    return {"mensagem": "API da IntuitiveCare ativa!"}

@app.get("/buscar")
def buscar_operadoras(termo: str = Query(..., min_length=2)):
    termo_lower = termo.lower()

    resultados = df[
        df["Razao_Social"].fillna("").str.lower().str.contains(termo_lower) |
        df["Nome_Fantasia"].fillna("").str.lower().str.contains(termo_lower)
    ]

    # Remove NaNs antes de converter para JSON
    resultados = resultados.fillna("")

    return resultados.head(20).to_dict(orient="records")

