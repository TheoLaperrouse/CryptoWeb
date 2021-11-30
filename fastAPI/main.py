from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/binance")
def read_binance(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/polychain")
def read_polychain():
    return {"type":"Unicorn","color":"blue"}

@app.get("/maiar")
def read_maiar():
    return {"EGLD":0}