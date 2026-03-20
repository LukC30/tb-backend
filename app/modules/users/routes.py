from fastapi import APIRouter, Depends
from ...core.dependencies import get_user_service
from ..users.service import UserService

from .schema import MembroRequest


user_router = APIRouter(
    prefix="/v1/member",
    tags=["member"]
)

@user_router.post("/", status_code=201)
async def create_member(member_request: MembroRequest, user_service: UserService = Depends(get_user_service)):
    user = await user_service.create(member_request)
    return user

@user_router.get("/all-users", status_code=200)
async def get_users(user_service: UserService = Depends(get_user_service)):
    users = await user_service.get_all()
    return users


