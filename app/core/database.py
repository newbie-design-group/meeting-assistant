# app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL settings
db_user = "your_db_user"
db_password = "your_db_password"
db_host = "localhost"
db_port = "5432"
db_name = "meeting_assistant"

DATABASE_URL = (
    f"postgresql://{db_user}:{db_password}@"
    f"{db_host}:{db_port}/{db_name}"
)

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
Base = declarative_base()