from fastapi import APIRouter, Depends
from .schema import CreateLoginRequest
from ...core.dependencies import get_auth_service


auth_route = APIRouter(
    prefix='/v1/auth'
)

@auth_route.post('/')
async def create_login(create_user: CreateLoginRequest, auth_service = Depends(get_auth_service)):
    user