# Connecting MySQL database
# create_engine is a function that is the central entry point for sqlalchemy db connection

from sqlalchemy import create_engine
from urllib.parse import quote_plus
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

class Database:
    def __init__(self):
        self.engine = None
        self.SessionLocal = None
        self.Base = declarative_base()

    def loadingFiles(self):
        try:
            load_dotenv()
        except ModuleNotFoundError:
            print("No such module exists.")

        self.USER = os.getenv("USERNAME")
        self.PASSWORD = os.getenv("PASSWORD")
        self.DATABASE = os.getenv("DATABASE")

        self.pw = quote_plus(self.PASSWORD)

    def connectingDatabase(self):
        try:
            self.engine = create_engine(f"mysql+pymysql://{self.USER}:{self.pw}@localhost/{self.DATABASE}", pool_pre_ping=True)
        except Exception as e:
            print("Error connecting to database", e)
        
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


# Creating a single reusable database instance
db_instance = Database()
db_instance.loadingFiles()
db_instance.connectingDatabase()

SessionLocal = db_instance.SessionLocal
Base = db_instance.Base
engine = db_instance.engine

# Dependency function for fast API
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close
