from abc import ABC, abstractmethod
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.auth.model import Login

class BaseAuthRepository(ABC):
    def __init__(self, db: AsyncSession):
        self.db = db

    @abstractmethod 
    async def create(self, login_model: Login) -> Optional[Login]:
        pass
    
    @abstractmethod
    async def update(self, login_model: Login) -> Optional[Login]:
        pass