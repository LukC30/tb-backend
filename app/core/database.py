from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_BASE_URL = """mysql+asyncmy://root:@localhost:3306/db_desbravadores"""

engine = create_async_engine(
    SQLALCHEMY_BASE_URL,
    echo=True
)

AsyncSessionLocal = async_sessionmaker(class_=AsyncSession, autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

async def get_db():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            db.close()