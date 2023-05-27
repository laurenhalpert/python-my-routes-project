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
    view_my_info,
    edit_my_info,
    update_my_info,
    update_message
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
        print(f'Hello, {name}.')
        print('What actions would you like to take today?')
        menu = input('"view my info", "view my flight info", "change my flight", "cancel my flight", or "exit": ')
        if menu == 'view my info':
            print('Here is your info: ')
            view_my_info(name)
            edit_choice = input('Would you like to edit your info? y/n : ')
            if edit_choice == 'y':
                edit = input('Name, Age :')
                edit
            elif edit_choice == 'n':
                # menu = input('"view my info", "view my flight info", "change my flight", "cancel my flight", or "exit": ')
                # menu
                print(f'Thanks for visiting {name}. Goodbye!')

    # if retrieve_passenger_info(name):
    #     print (f'Hello, {name}.')
    #     show_menu()
    #     if show_menu() == "view my info":
    #         view_my_info(name)
    #         if view_my_info(name) == 'y':
    #             edit_my_info()
    #             edited_info = edit_my_info()
    #             update_my_info(edited_info)
    #             update_message()
    #             if update_message() == 'y':
    #                 show_menu()
    #             elif update_message() == 'n':
    #                 edit_my_info()
    #                 edited_info = edit_my_info()
    #                 update_my_info(edited_info)
    #                 update_message()
    #         elif view_my_info(name) == 'n':
    #             show_menu()
        

    # else:
    #     print (f'It looks like there is no flight reservation under that name. Would you like to make a reservation?')
    # update_flight_report(passenger_flights)