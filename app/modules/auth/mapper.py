from .schema import CreateLoginRequest
from .model import Login

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
    def to_response(auth_model, user_model):
        