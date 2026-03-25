from datetime import date
from pydantic import BaseModel

class CreateLoginRequest(BaseModel):
    email: str
    senha: str
    nome: str
    telefone: str
    data_nascimento: date

class CreateLoginResponse(BaseModel):
    id: str
    email: str
