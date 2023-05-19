# from faker import Faker
# import random

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from models import Airline, Route, Passenger, Plane, plane_passenger

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///trip.db')
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     fake = Faker()

#     dep_cities = [
#         'Denver', 'Houston', 'San Francisco', 'Portland', 'Boston',
#          'Chicago', 'Miami', 'Nashville', 'Phoenix', 'Des Moines', 'San Diego'
#     ]
#     arr_cities = [
#         'Los Angeles', 'Anchorage', 'Dallas', 'Salt Lake City', 'Seattle',
#         'Detroit', 'Charleston', 'St. Louis', 'Kansas City', 'Omaha'
#     ]
#     plane_types = ['737', '757', '787', 'A321']
#     airline_names = [
#         "FlyFly", "Aero", "Wings", "SkyDragon", "Air Python"
#     ]

#     routes = []
#     for i in range(50):
#         route = Route(
#             departure_city=random.choice(dep_cities),
#             arrival_city=random.choice(arr_cities),
#             departure_time=random.randint(1600, 1659),
#             arrival_time=random.randint(2000, 2059)
#         )

#         session.add(route)
#         session.commit()

#         routes.append(route)
#     planes = []
#     for route in routes:
#         plane = Plane(
#             plane_type = random.choice(plane_types),
#             passenger_limit = random.randint(120, 300)
#         )
   
#     airlines=[]
#     passengers = []
#     for plane in planes:
#         for i in range(plane.passenger_limit):
#             passenger = Passenger(
#                 passenger_name = fake.unique.name(),
#                 passenger_age = random.randint(15, 90)
#             )
#         passengers.append(passenger)
#         airline = Airline(
#             airline_name=random.choice(airline_names)
#         )
#         airlines.append(airline)
#     session.bulk_save_objects(airlines, passengers)
#     session.commit()
#     session.close()
            
    


            
