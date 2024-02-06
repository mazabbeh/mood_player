import os
from dotenv import load_dotenv
load_dotenv()
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f'sqlite:///app.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)