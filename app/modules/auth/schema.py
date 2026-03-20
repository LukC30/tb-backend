from datetime import date
from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str
    senha: str
    name: str
    telefone: str
    data_nascimento: date