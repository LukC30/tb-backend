from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .interface import BaseUserRepository
from .model import Membro

class UserRepository(BaseUserRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, member: Membro):
        self.db.add(member)
        await self.db.commit()
        await self.db.refresh(member)
        return member
    
    async def get_by_id(self, id) -> Optional[Membro]:
        query = select(Membro).where(Membro.id == id)
        member = await self.db.execute(query)
        return member.scalars().first() 
    
    async def get_all(self):
        query = select(Membro)
        members_data = await self.db.execute(query)
        members_list = members_data.scalars().all()
        return members_list