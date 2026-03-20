from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging

from app.core.database import engine, Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("[SERVER] Iniciando aplicação...")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield
    logging.info("[SERVER] Encerrando aplicação...")
    
    await engine.dispose()