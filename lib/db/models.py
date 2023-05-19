from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///many_to_many.db')

Base = declarative_base()

plane_passenger = Table(
    'plane_passengers',
    Base.metadata,
    Column('plane_id', ForeignKey('planes.id'), primary_key = True),
    Column('passenger_id', ForeignKey('passenger.id'), primary_key = True),
    extend_existing = True
)


class Airline(Base):
    __tablename__ = 'airlines'

    id = Column(Integer(), primary_key = True),
    airline_name = Column(String())

    def __repr__(self):
        print(f'Airline, {airline_name}, has id {id}')

class Route(Base):
    __tablename__ = 'routes'

    id = Column(Integer(), primary_key = True),
    departure_city = Column(String()),
    arrival_city = Column(String()),
    departure_time = Column(DateTime()),
    arrival_time = Column(DateTime())

    def __repr__(self):
        print(f'Route {departure_city} to {arrival_city} has id {id}. It departs at {departure_time} and arrives at {arrival_time}.')


class Plane(Base):
    __tablename__ = 'planes'

    id = Column(Integer(), primary_key = True),
    airline_id = Column(ForeignKey('airlines.id')),
    route_id = Column(ForeignKey('routes.id')),
    plane_type = Column(String()),
    passenger_limit = Column(Integer())

    airline = relationship('Airline', back_populates = 'planes')
    route = relationship('Route', back_populates = 'planes')

    passengers = relationship('Passenger', secondary = plane_passenger, back_populates = 'planes')

    def __repr__(self):
        print(f'Plane, {plane_type}, operated by {airline.airline_name}, is going on route {route.departure_city}-{route.arrival_city} and has a passenger limit of {passenger_limit}. The passengers on this plane are: {passengers}.')

class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer(), primary_key = True),
    passenger_name = Column(String()),
    passenger_age = Column(Integer())

    planes = relationship('Plane', secondary = plane_passenger, back_populates= 'passengers')

    def __repr__(self):
        print(f'Passenger, {passenger_name} is {passenger_age} years old and has id of {id}.')

