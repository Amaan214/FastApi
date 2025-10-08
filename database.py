# Connecting MySQL database
# create_engine is a function that is the central entry point for sqlalchemy db connection

from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

pw = quote_plus(PASSWORD)

engine = create_engine(f"mysql+pymysql://{USER}:{pw}@localhost/{DATABASE}", pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()