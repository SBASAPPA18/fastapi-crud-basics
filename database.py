from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:Sharana%4018@localhost:5432/practice"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False,autoflush=False,bind=engine)
