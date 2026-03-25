from ..modules.users.repository import UserRepository
from app.modules.users.service import UserService

from ..modules.auth.repository import AuthRepository
from ..modules.auth.service import AuthService


from .database import get_db

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

# Injeção de repositories
def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)

def get_auth_repository(db: AsyncSession = Depends(get_db)) -> AuthRepository:
    return AuthRepository(db)

# Injeção de services
def get_user_service(user_repo = Depends(get_user_repository)) -> UserService:
    return UserService(user_repo)

def get_auth_service(auth_repo = Depends(get_auth_repository), user_repo = Depends(get_user_repository)) -> AuthService:
    return AuthService(auth_repo, user_repo)