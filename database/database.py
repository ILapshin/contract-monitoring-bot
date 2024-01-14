from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from config import DB_URL

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()
