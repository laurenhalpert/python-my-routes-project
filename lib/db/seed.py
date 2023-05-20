from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Airline, Route, Passenger, Plane

if __name__ == '__main__':
    engine = create_engine('sqlite:///trip.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    fake = Faker()

    dep_cities = [
        'Denver', 'Houston', 'San Francisco', 'Portland', 'Boston',
         'Chicago', 'Miami', 'Nashville', 'Phoenix', 'Des Moines', 'San Diego'
    ]
    arr_cities = [
        'Los Angeles', 'Anchorage', 'Dallas', 'Salt Lake City', 'Seattle',
        'Detroit', 'Charleston', 'St. Louis', 'Kansas City', 'Omaha'
    ]
    plane_types = ['737', '757', '787', 'A321']
    airline_names = [
        "FlyFly", "Aero", "Wings", "SkyDragon", "Air Python"
    ]

    routes = []
    for i in range(50):
        route = Route(
            departure_city=random.choice(dep_cities),
            arrival_city=random.choice(arr_cities),
            departure_time=random.randint(1600, 1659),
            arrival_time=random.randint(2000, 2059)
        )

        session.add(route)
        session.commit()

        routes.append(route)

    planes = []
    for i in range(50):
        plane = Plane(
            plane_type = random.choice(plane_types),
            passenger_limit = random.randint(120, 300)
        )
        session.add(plane)
        session.commit()
        planes.append(plane)

    passengers = []
    for i in range(1000):
        passenger = Passenger(
            passenger_name = fake.unique.name(),
            passenger_age = random.randint(15,90)
        )
        session.add(passenger)
        session.commit()
        passengers.append(passenger)
    
    airlines =[]
    for i in range(5):
        airline = Airline(
            airline_name=airline_names[i]
        )
        session.add(airline)
        session.commit()

        airlines.append(airline)
    
    session.close()
            
    


            
