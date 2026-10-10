from fastapi import FastAPI, status
from pydantic import BaseModel
import src.clientdata.database as db

app = FastAPI()

class ClientSchema(BaseModel):
    name: str
    endereco: str
    qtd_pedidos: int = 0
    valor_pedidos: float = 0.0

@app.get("/")
def home():
    return {"mensagem": "A api esta rodando???!" "Sim esta"}

# Cria a rota clientes e me retorna os dados do db
@app.get("/clientes")
def listar_clientes():
    clientes = db.todos_clientes()

    return clientes

@app.post("/clientes", status_code=status.HTTP_201_CREATED)
def cad_clientes(cliente: ClientSchema):
    return db.add_client(cliente.model_dump())            