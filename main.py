from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session
from app.crud import search_providers, handle_question

app = FastAPI()

@app.get("/providers")
async def get_providers(
    drg: str,
    zip: str,
    radius_km: int = 50,
    db: AsyncSession = Depends(get_session)
):
    return await search_providers(db, drg, zip, radius_km)

@app.post("/ask")
async def ask(data: dict, db: AsyncSession = Depends(get_session)):
    return await handle_question(data["question"], db)
