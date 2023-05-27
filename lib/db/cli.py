#!/usr/bin/env python3
# class MyFlight:
#     def __init__(self, user_input):
#         self.value = user_input

# move to helpers.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Airline, Route, Passenger, Plane
from helpers import (
    retrieve_passenger_info,
    show_menu,
    view_my_info
)

engine = create_engine('sqlite:///trip.db')
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # passenger_flights = []

    name = input('Please enter your name: ')
    # while name:
    #     passenger_flights.append(name)
        #  name = input('Please enter your name: ')
    retrieve_passenger_info(name)
    if retrieve_passenger_info(name):
        print (f'Hello, {name}. What actions would you like to take today?')
        show_menu()
        if show_menu() == "view my info":
            view_my_info(name)
        

    # else:
    #     print (f'It looks like there is no flight reservation under that name. Would you like to make a reservation?')
    # update_flight_report(passenger_flights)