"""creating a database for news"""

import os
from pathlib import Path
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# setting working directory
WORK_DIR = Path(__file__).parent.parent

# getting all the information we need from .env
load_dotenv(WORK_DIR / ".env")
USERNAME = os.getenv("MYSQL_USERNAME")
PASSWORD = os.getenv("MYSQL_PASSWORD")

# mysql connector
DB_URL = f"mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost:3306/news"

# creating the engine
engine = create_engine(DB_URL)

# Base for NewsDara class
Base = declarative_base()

# making the session
Session = sessionmaker(bind=engine)
session = Session()


class NewsData(Base):
    """table for database"""
    __tablename__ = 'news' #name of the table
    id = Column(Integer, primary_key=True)
    Title = Column(String(300), nullable=False)
    Url = Column(String(300), nullable=False)

Base.metadata.create_all(engine)
