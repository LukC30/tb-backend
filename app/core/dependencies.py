from ..modules.users.repository import UserRepository
from app.modules.users.service import UserService
from .database import get_db

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_user_service(user_repo = Depends(get_user_repository)) -> UserService:
    return UserService(user_repo)