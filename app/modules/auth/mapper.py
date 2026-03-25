from .schema import CreateLoginRequest, CreateLoginResponse
from .model import Login
from ..users.model import Membro
class AuthMapper():

    @staticmethod
    def create_login_to_model(id_user: int, create_login_request: CreateLoginRequest):
        return Login(
            email=create_login_request.email,
            senha=create_login_request.senha,
            id_user=id_user,
        )

    @staticmethod
    def to_model():
        pass

    @staticmethod
    def to_response(auth_model: Login, user_model: Membro):
        pass