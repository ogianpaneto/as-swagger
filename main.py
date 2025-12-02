from fastapi import FastAPI
from datetime import datetime


app = FastAPI(
    title="API de Demonstração Swagger",
    description="API para demonstrar documentação viva",
    version="2.0.0"
)


@app.get("/")
def root():
    return {"message": "API de teste"}

@app.get("/date/day", tags=["Date"])
def get_data_dia():
    """Retorna a data atual no formato AAAA-MM-DD"""
    return {"datetime": datetime.now().strftime("%Y-%m-%d")}

@app.get("/date/time", tags=["Date"])
def get_data_hora():
    """Retorna a hora atual no formato HH:MM:SS"""
    return {"datetime": datetime.now().strftime("%H:%M:%S")}

@app.get("/math/sum", tags=["Math"])
def soma_numeros(a: int, b: int):
    """Retorna a soma de dois números inteiros"""
    return {"result": a + b}