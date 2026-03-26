from fastapi import APIRouter, Depends
from .schema import CreateLoginRequest
from ...core.dependencies import get_auth_service
from .service import AuthService

auth_router = APIRouter(
    prefix='/v1/auth'
)

@auth_router.post('/')
async def create_login(create_user: CreateLoginRequest, auth_service: AuthService = Depends(get_auth_service)):
    user = await auth_service.create_user(create_user)
    return user