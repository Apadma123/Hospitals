import pandas as pd
import asyncio
import random
from tqdm import tqdm

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete

from app.database import async_session, engine
from app.models import Provider

# ✅ Clean, fast CSV load
def load_data():
    try:
        df = pd.read_csv(
            "data/sample_prices_ny.csv",
            encoding="utf-8"
        )
    except UnicodeDecodeError:
        print("⚠️ UTF-8 failed, retrying with Windows-1252 encoding...")
        df = pd.read_csv(
            "data/sample_prices_ny.csv",
            encoding="windows-1252",
            engine="python",
            on_bad_lines="skip"
        )

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df['ms_drg_definition'] = df['ms_drg_definition'].str.strip()
    df['provider_name'] = df['provider_name'].str.strip()
    return df


# ✅ Async ETL insert logic
async def run_etl():
    df = load_data()

    providers = []
    for row in tqdm(df.itertuples(), total=len(df)):
        try:
            provider = Provider(
                provider_id=int(row.provider_id),
                provider_name=row.provider_name,
                provider_city=row.provider_city,
                provider_state=row.provider_state,
                provider_zip_code=row.provider_zip_code,
                #ms_drg_definition=row.ms_drg_definition,
                #total_discharges=int(row.total_discharges),
                #average_covered_charges=float(row.average_covered_charges),
                #average_total_payments=float(row.average_total_payments),
                #average_medicare_payments=float(row.average_medicare_payments),
                #rating=random.randint(1, 10)  # generate mock rating
            )
            providers.append(provider)
        except Exception as e:
            print(f"⚠️ Skipping bad row: {e}")
            continue

    async with async_session() as session:
        # Optional: Wipe existing data
        await session.execute(delete(Provider))

        session.add_all(providers)
        await session.commit()
        print(f"✅ Inserted {len(providers)} providers.")


# ✅ Run the ETL
if __name__ == "__main__":
    try:
        asyncio.run(run_etl())
    except Exception as e:
        print(f"❌ ETL failed: {e}")
