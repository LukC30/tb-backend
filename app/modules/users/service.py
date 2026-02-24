from ..users.interface import BaseUserRepository

class UserService():
    def __init__(self, user_repo: BaseUserRepository):
        self.user_repo = user_repo

    
    async def create(self, user_request):
        pass