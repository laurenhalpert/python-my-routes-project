def create_flight_report(passenger_flights):
    with open('./cli.text', 'w') as fr:
        for flight in passenger_flights:
            fr.write(flight + '\n')