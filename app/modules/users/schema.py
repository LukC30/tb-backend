from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str
    telefone: str
    