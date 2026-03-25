from .interface import BaseAuthRepository
from .schema import CreateLoginRequest
from .mapper import AuthMapper
from .auth import password_encript

from ..users.repository import BaseUserRepository
from ..users.mapper import UserMapper


class AuthService():
    def __init__(self, auth_repo: BaseAuthRepository, user_repo: BaseUserRepository):
        self.auth_repo = auth_repo
        self.user_repo = user_repo

    async def create_user(self, create_login_request: CreateLoginRequest):
        create_login_request.senha = password_encript(create_login_request.senha)
        user_model = UserMapper.auth_to_model(create_login_request)
        user = await self.user_repo.create(user_model)

        auth_model = AuthMapper.create_login_to_model(user.id, create_login_request)
        auth = await self.auth_repo.create(auth_model)

        
        return auth