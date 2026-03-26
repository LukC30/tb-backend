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
        user = UserMapper.auth_to_model(create_login_request)
        user_model = await self.user_repo.create(user)

        auth = AuthMapper.create_login_to_model(user.id, create_login_request)
        auth_model = await self.auth_repo.create(auth)

        response = AuthMapper.to_response(auth_model, user_model)
        return response