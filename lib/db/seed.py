from faker import Faker
import random
from random import choice as rc

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Airline, Route, Passenger, Plane


engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

def delete_records():
    session.query(Airline).delete()
    session.query(Route).delete()
    session.query(Passenger).delete()
    session.query(Plane).delete()
    session.commit()


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

def create_records():
    routes = [
        Route(
            departure_city=random.choice(dep_cities),
            arrival_city=random.choice(arr_cities),
            departure_time=random.randint(1600, 1659),
            arrival_time=random.randint(2000, 2059)
        ) for i in range(50)
    ]
    planes = [
        Plane(
            plane_type = random.choice(plane_types),
            passenger_limit = random.randint(120, 300),
            airline_id = random.randint(1, 5),
            route_id = random.randint(1, 50)
        ) for i in range(50)
    ]
    passengers =[
        Passenger(
            passenger_name = fake.unique.name(),
            passenger_age = random.randint(15,90),
            plane_id = random.randint(1, 50)
        ) for i in range (3000)
    ]
    airlines = [
        Airline(
            airline_name=airline_names[i]
        ) for i in range(5)
    ]
    session.add_all(routes + planes + passengers + airlines)
    session.commit()
    return routes, planes, passengers, airlines

def relate_records(routes, planes, airlines, passengers):
    for plane in planes:
        plane.airline = rc(airlines)
        plane.route = rc(routes)

    for passenger in passengers:
        passenger.plane = rc(planes)

    session.add_all(planes + passengers)
    session.commit()

if __name__ == '__main__':
    delete_records()
    routes, planes, passengers, airlines = create_records()
    relate_records(routes, planes, airlines, passengers)
    # routes = []
    # for i in range(50):
    #     route = Route(
    #         departure_city=random.choice(dep_cities),
    #         arrival_city=random.choice(arr_cities),
    #         departure_time=random.randint(1600, 1659),
    #         arrival_time=random.randint(2000, 2059)
    #     )

    #     session.add(route)
    #     session.commit()
        
    #     routes.append(route)

    # planes = []
    # for i in range(50):
    #     plane = Plane(
    #         plane_type = random.choice(plane_types),
    #         passenger_limit = random.randint(120, 300),
    #         airline_id = random.randint(1, 5),
    #         route_id = random.randint(1, 50)
    #     )
    #     session.add(plane)
    #     session.commit()
        
    #     planes.append(plane)

    # passengers = []
    # for i in range(1000):
    #     passenger = Passenger(
    #         passenger_name = fake.unique.name(),
    #         passenger_age = random.randint(15,90),
    #         plane_id = random.randint(1, 50)
    #     )
    #     session.add(passenger)
    #     session.commit()
        
    #     passengers.append(passenger)
    
    # airlines =[]
    # for i in range(5):
    #     airline = Airline(
    #         airline_name=airline_names[i]
    #     )
    #     session.add(airline)
    #     session.commit()
        
    #     airlines.append(airline)
    
    # session.close()
            
    


            
