from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class BaseAuthRepository(ABC):
    def __init__(self, db: AsyncSession):
        self.db = db

    @abstractmethod 
    async def create():
        pass
