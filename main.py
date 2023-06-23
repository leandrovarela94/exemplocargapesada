from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Msg(BaseModel):
    msg: str


@app.get("/health")
def get_health():
    return {"titulos":"Foi indicado pela FIFA ao seleto grupo dos maiores clubes do século XX. Dentre seus principais títulos no futebol estão: 21 Campeonatos Cariocas, quatro Torneios Rio-São Paulo, duas Taças dos Campeões Estaduais Rio-São Paulo, dois Campeonatos Brasileiros e uma Copa CONMEBOL (precursora da atual Copa Sul-Americana)."}
