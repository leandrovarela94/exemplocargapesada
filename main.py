from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str


@app.get("/health")
def get_health():
    return "APLICAÇÃO RODANDO"
