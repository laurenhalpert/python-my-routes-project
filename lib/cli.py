#!/usr/bin/env python3
# class MyFlight:
#     def __init__(self, user_input):
#         self.value = user_input

# move to helpers.py
from helpers import create_flight_report

if __name__ == '__main__':
    passenger_flights = []

    flight = input('Passenger name, departure_city, arrival_city, plane type, airline')
    while flight:
        passenger_flights.append(flight)
        flight = input('Passenger name, departure_city, arrival_city, plane type, airline')
    create_flight_report(passenger_flights)