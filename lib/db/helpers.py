from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker

from models import Airline, Route, Passenger, Plane

# view my info
# view my flight info
# change my route
# cancel my flight
# transfer my flight to someone else


engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

def retrieve_passenger_info(input):
    name = text(input)
    
    passenger = session.query(Passenger).filter(Passenger.passenger_name.like(f'%{name}%')).all()
    return passenger[0]
    