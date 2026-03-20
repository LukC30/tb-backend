from .interface import BaseAuthRepository

class UserRepository(BaseAuthRepository):
    def __init__(self, db):
        super().__init__(db)

    async def create():
        pass