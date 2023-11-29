from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import config

Base = declarative_base()

DB_URL = config.DB_URL
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(engine)
