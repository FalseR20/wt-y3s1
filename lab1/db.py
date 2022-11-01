from pathlib import Path

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = Path(__file__).resolve().parent.joinpath("sqlite.db")
engine = sa.create_engine(f"sqlite:////{DB_PATH.absolute()}", echo=True)
Base = declarative_base()


class Employee(Base):
    __tablename__ = "Employee"
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, default="unnamed")
    place = sa.Column(sa.String, default="unknown")


Base.metadata.create_all(engine)
Session = sessionmaker(engine)
