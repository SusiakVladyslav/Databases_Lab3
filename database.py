from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

hostname = os.environ.get("hostname")
database = os.environ.get('database')
username = os.environ.get('psql_username')
pwd = os.environ.get('pwd')
port_id = str(os.environ.get('port_id'))


DATABASE_URL = f"postgresql+psycopg2://{username}:{pwd}@{hostname}:{port_id}/{database}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
