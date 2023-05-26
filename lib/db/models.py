from sqlalchemy import create_engine, func, MetaData
from sqlalchemy import ForeignKey, Table, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Plane(Base):
    __tablename__ = 'planes'

    # def __init__(self, airline_id, route_id, plane_type, passenger_limit, id = None):
    #     self.id = id
    #     self.airline_id = Column(Integer(), ForeignKey('airlines.id'))
    #     self.route_id = Column(Integer(), ForeignKey('routes.id'))
    #     self.plane_type = plane_type
    #     self.passenger_limit = passenger_limit

    id = Column(Integer(), primary_key = True)
    
    plane_type = Column(String())
    passenger_limit = Column(Integer())

    airline_id = Column(ForeignKey('airlines.id'))
    route_id = Column(ForeignKey('routes.id'))

    # airline = relationship('Airline', backref = backref('plane'))
    # route = relationship('Route', backref = backref('plane'))

    #Plane & Passengers have a one to many relationship
    passengers = relationship('Passenger', backref='plane')
    

    def __repr__(self):
        return f'Plane: {self.plane_type}'
        # return(f'Plane, {plane.plane_type}, operated by {airline.airline_name}, is going on route {route.departure_city}-{route.arrival_city} and has a passenger limit of {passenger_limit}. The passengers on this plane are: {passengers}.')

class Airline(Base):
    __tablename__ = 'airlines'

    # def __init__(self, airline_name, id = None):
    #     self.id = id
    #     self.airline_name = airline_name

    id = Column(Integer(), primary_key = True)
    airline_name = Column(String())

    # planes = relationship('Plane', backref = backref('airline'))
    planes = relationship('Plane', backref = 'airline')
    routes = association_proxy('planes', 'route',
        creator=lambda rt: Plane(route=rt))

    def __repr__(self):
        return(f'Airline, {self.airline_name}, has id {self.id}')

class Route(Base):
    __tablename__ = 'routes'

    # def __init__(self, departure_city, arrival_city, departure_time, arrival_time, id = None):
    #     self.id = id
    #     self.departure_city = departure_city
    #     self.arrival_city = arrival_city
    #     self.departure_time = departure_time
    #     self.arrival_time = arrival_time

    id = Column(Integer(), primary_key = True)
    departure_city = Column(String())
    arrival_city = Column(String())
    departure_time = Column(Integer())
    arrival_time = Column(Integer())

    # planes = relationship('Plane', backref = backref('route'))
    planes = relationship('Plane', backref = 'route')
    airlines = association_proxy('planes', 'airline',
        creator=lambda al: Freebie(airline=al))


    def __repr__(self):
        return(f'Route {self.departure_city} to {self.arrival_city}')


class Passenger(Base):
    __tablename__ = 'passengers'

    # def __init__(self, passenger_name, passenger_age, plane_id, id = None):
    #     self.id = id
    #     self.passenger_name = passenger_name
    #     self.passenger_age = passenger_age
    #     self.plane_id = Column(Integer(), ForeignKey('planes.id'))

    id = Column(Integer(), primary_key = True)
    passenger_name = Column(String())
    passenger_age = Column(Integer())
    plane_id = Column(ForeignKey('planes.id'))

    
    # plane = relationship('Plane', backref='passenger')
    

    def __repr__(self):
        return f'Passenger: {self.passenger_name}'

