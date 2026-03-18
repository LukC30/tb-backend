from .schema import MembroRequest
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