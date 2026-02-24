from abc import ABC, abstractmethod
from .model import Membro
from typing import Optional

class BaseUserRepository(ABC):
    
    @abstractmethod
    async def create(self, member: Membro):
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[Membro]:
        pass
    
    @abstractmethod
    async def get_all(self) -> list[Membro]:
        pass