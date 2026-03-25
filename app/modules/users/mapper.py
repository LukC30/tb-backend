from .domain import CargoMembro
from .schema import MembroRequest
from ..auth.schema import CreateLoginRequest
from .model import Membro

class UserMapper():

    @staticmethod
    def to_model(member_request: MembroRequest):
        member = Membro(
            nome=member_request.name,
            cargo=member_request.cargo,
            data_nascimento=member_request.data_nascimento,
            telefone=member_request.telefone
        )

        return member
    
    @staticmethod
    def auth_to_model(create_login_request: CreateLoginRequest):
        return Membro(
            nome=create_login_request.nome,
            cargo=CargoMembro.DESBRAVADOR,
            data_nascimento=create_login_request.data_nascimento,
            telefone=create_login_request.telefone
        )

    # @staticmethod
    # def to_