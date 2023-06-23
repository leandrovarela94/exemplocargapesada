from fastapi import FastAPI
from pydantic import BaseModel

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
    return "APLICAÇÃO RODANDO"
