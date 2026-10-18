from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine=create_engine(DATABASE_URL, echo=False, pool_pre_ping=True )
SessionLocal=sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

