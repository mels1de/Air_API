from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession,AsyncEngine,create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine:AsyncEngine = create_async_engine(
    str(settings.DATABASE_URL),
    echo = settings.DEBUG,
    future=True
)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session