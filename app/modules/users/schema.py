from pydantic import BaseModel
from .domain import CargoMembro
from datetime import date

class MembroRequest(BaseModel):
    name: str
    telefone: str
    cargo: CargoMembro
    data_nascimento: date
