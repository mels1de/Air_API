from fastapi import FastAPI,Depends,HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.db.session import get_db
from app.core.config import settings


app = FastAPI(title=settings.APP_NAME)

@app.get("/health")
async def health(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    if result.scalar() == 1:
        return {"status": "OK"}
    raise HTTPException(500, "db connection failed")



