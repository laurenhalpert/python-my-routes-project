from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///many_to_many.db')

Base = declarative_base()

class Airline(Base):
    __tablename__ = 'airlines'

    id = Column(Integer(), primary_key = true),
    airline_name = Column(String())

    def __repr__(self):
        print(f'Airline, {airline_name}, has id {id}')