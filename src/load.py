import logging
import os
from sqlalchemy import create_engine

logger = logging.getLogger(__name__)

def load_to_postgres(df):
    host=os.getenv("POSTGRES_HOST","postgres"); port=os.getenv("POSTGRES_PORT","5432")
    user=os.getenv("POSTGRES_USER","etl_user"); password=os.getenv("POSTGRES_PASSWORD","etl_password"); db=os.getenv("POSTGRES_DB","air_quality")
    engine=create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")
    out=df.copy(); out["timestamp_local"]=out["timestamp_local"].dt.strftime("%Y-%m-%d %H:%M:%S")
    out.to_sql("air_quality", engine, if_exists="append", index=False, method="multi")
    logger.info("Loaded %s rows into PostgreSQL", len(out))
