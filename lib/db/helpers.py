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
    return( passenger[0] )
    
def show_menu():
    print('What actions would you like to take today?')
    menu = input('"view my info", "view my flight info", "change my flight", "cancel my flight", or "exit": ')
    return menu

def view_my_info(name):
    my_info = session.query(Passenger).filter(Passenger.passenger_name.like(f'%{name}%')).all()
    print(f'Name: {name} Age: {my_info[0].passenger_age}')
    # option_to_edit = input('Would you like to edit your info? y/n: ')
    # return option_to_edit

def edit_my_info():
    edit = input('Name, Age :')
    return edit

def update_my_info(personal_info):
    # do something to update the db with the new personal_info
    pass

def update_message():
    print('Here is your updated info:')
    view_my_info()
    confirm_edited_info= input('Is this correct? y/n')
    return confirm_edited_info
