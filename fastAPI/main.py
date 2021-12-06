from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from binance_infos import get_infos

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/binance")
def read_binance():
    return get_infos()

@app.get("/polychain")
def read_polychain():
    return {"type": "Unicorn", "color": "blue"}

@app.get("/maiar")
def read_maiar():
    return {"EGLD": 0}
