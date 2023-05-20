from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///trip.db')

Base = declarative_base()


class Airline(Base):
    __tablename__ = 'airlines'

    id = Column(Integer(), primary_key = True)
    airline_name = Column(String())

    def __repr__(self):
        print(f'Airline, {airline_name}, has id {id}')

class Route(Base):
    __tablename__ = 'routes'

    id = Column(Integer(), primary_key = True)
    departure_city = Column(String())
    arrival_city = Column(String())
    departure_time = Column(Integer())
    arrival_time = Column(Integer())

    def __repr__(self):
        print(f'Route {departure_city} to {arrival_city} has id {id}. It departs at {departure_time} and arrives at {arrival_time}.')


class Plane(Base):
    __tablename__ = 'planes'

    id = Column(Integer(), primary_key = True)
    airline_id = Column(ForeignKey('airlines.id'))
    route_id = Column(ForeignKey('routes.id'))
    plane_type = Column(String())
    passenger_limit = Column(Integer())

    # airline = relationship('Airline', backref = backref('plane'))
    # route = relationship('Route', backref = backref('plane'))

    #Plane & Passengers have a one to many relationship
    # passengers = relationship('Passenger', backref=backref('plane'))
    

    def __repr__(self):
        print(f'Plane, {plane_type}, operated by {airline.airline_name}, is going on route {route.departure_city}-{route.arrival_city} and has a passenger limit of {passenger_limit}. The passengers on this plane are: {passengers}.')

class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer(), primary_key = True)
    passenger_name = Column(String())
    passenger_age = Column(Integer())
    

    

    

    def __repr__(self):
        print(f'Passenger, {passenger_name} is {passenger_age} years old and is on plane {plane.plane_type}.')

