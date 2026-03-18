from .interface import BaseUserRepository
from .schema import MembroRequest
from .mapper import UserMapper

class UserService():
    def __init__(self, user_repo: BaseUserRepository):
        self.user_repo = user_repo

    async def create(self, user_request: MembroRequest):
        member_model = UserMapper.to_model(user_request)
        member_data = await self.user_repo.create(member_model)
        return member_data

        