from app.modules.auth.model import Login

from .interface import BaseAuthRepository

class AuthRepository(BaseAuthRepository):
    def __init__(self, db):
        super().__init__(db)

    async def create(self, login_model: Login):
        self.db.add(login_model)
        await self.db.commit()
        await self.db.refresh(login_model)
        return login_model
    
    async def update(self, login_model: Login):
        pass