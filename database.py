import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://postgres:password@host.docker.internal:5432/DunderMifflin"
db = create_engine(db_string)
base = declarative_base()


class Warehouse(base):
    __tablename__ = 'warehouse'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)
