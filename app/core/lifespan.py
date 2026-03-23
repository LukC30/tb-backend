from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from app.core.database import engine, Base
from app.modules.users.model import Membro
from app.modules.auth.model import Login
from app.modules.unidade.model import Unidade, MembroUnidade


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("[SERVER] Iniciando aplicação...")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    logging.info("[SERVER] Encerrando aplicação...")
    
    await engine.dispose()