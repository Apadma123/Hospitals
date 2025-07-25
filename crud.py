from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app.models import Provider, Procedure, Rating
from app.utils import get_coordinates, haversine_distance
from app.openai_assistant import ask_openai


async def search_providers(db: AsyncSession, drg: str, zip: str, radius_km: int):
    user_lat, user_lon = await get_coordinates(zip)

    stmt = (
        select(Provider, Procedure, Rating)
        .join(Procedure, Provider.provider_id == Procedure.provider_id)
        .join(Rating, Provider.provider_id == Rating.provider_id)
        .where(Procedure.ms_drg_definition.ilike(f"%{drg}%"))
    )

    results = await db.execute(stmt)
    rows = results.all()

    providers = []
    for provider, procedure, rating in rows:
        if provider.latitude and provider.longitude:
            distance = haversine_distance(user_lat, user_lon, provider.latitude, provider.longitude)
            if distance <= radius_km:
                providers.append({
                    "name": provider.provider_name,
                    "city": provider.provider_city,
                    "rating": rating.rating,
                    "distance_km": round(distance, 2),
                    "avg_covered_charges": procedure.average_covered_charges,
                    "drg": procedure.ms_drg_definition
                })

    sorted_providers = sorted(providers, key=lambda x: x["avg_covered_charges"])
    return sorted_providers

async def handle_question(question: str, db: AsyncSession):
    if any(word in question.lower() for word in ["weather", "sports", "news"]):
        return {"answer": "I can only help with hospital pricing and quality information."}

    sql_or_text = await ask_openai(question)
    # (Optional) You can try to parse and run SQL here
    return {"response": sql_or_text}
