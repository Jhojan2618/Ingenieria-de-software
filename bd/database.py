import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

sqlite_name = "Alquiler.sqlite"

base_dir = os.path.dirname(os.path.abspath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_name)}"

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
