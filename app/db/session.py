from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# SQLAlchemy engine
engine = create_engine(
    settings.database_url,
    future=True,
    echo=True, # print SQL queries in console (turn to false for prod)
)

# Session factory
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

# Base model class
class Base(DeclarativeBase):
    pass