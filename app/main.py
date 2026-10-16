from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ItemEntrada(BaseModel):
    nome: str
    quantidade: int = 1
    comprado: bool = False

itens = [
    {"id": 1, "nome": "Arroz", "quantidade": 2, "comprado": True},
    {"id": 2, "nome": "Feijão", "quantidade": 3, "comprado": True},
    {"id": 3, "nome": "Leite", "quantidade": 6, "comprado": False},
    {"id": 4, "nome": "Pão de forma", "quantidade": 1, "comprado": False},
    {"id": 5, "nome": "Café", "quantidade": 2, "comprado": False},
    {"id": 6, "nome": "Ovos (dúzia)", "quantidade": 2, "comprado": True},
    {"id": 7, "nome": "Banana (kg)", "quantidade": 1, "comprado": False},
    {"id": 8, "nome": "Sabão em pó", "quantidade": 1, "comprado": False},
]


@app.get("/")
def raiz():
    return {"mensagem": "API de itens funcionando"}


@app.get("/itens")
def listar_itens():
    return itens


@app.get("/itens/{item_id}")
def buscar_item(item_id: int):
    for item in itens:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.post("/itens", status_code=201)
def criar_item(entrada: ItemEntrada):
    novo_id = max((item["id"] for item in itens), default=0) + 1
    novo_item = {"id": novo_id, **entrada.model_dump()}
    itens.append(novo_item)
    return novo_item


@app.put("/itens/{item_id}")
def atualizar_item(item_id: int, entrada: ItemEntrada):
    for item in itens:
        if item["id"] == item_id:
            item.update(entrada.model_dump())
            return item
    raise HTTPException(status_code=404, detail="Item não encontrado")


@app.delete("/itens/{item_id}")
def apagar_item(item_id: int):
    for item in itens:
        if item["id"] == item_id:
            itens.remove(item)
            return {"mensagem": "Item apagado com sucesso"}
    raise HTTPException(status_code=404, detail="Item não encontrado")