#!/usr/bin/python3
"""List all states"""


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        exit(1)

    # Extracting command line arguments
    u = argv[1]
    p = argv[2]
    dbname = argv[3]

    # Creating engine and establishing connection
    engine = create_engine(
        f'mysql+mysqldb://{u}:{p}@localhost:3306/{dbname}',
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying cities and states
    results = session.query(City, State).\
        filter(City.state_id == State.id).all()

    # Printing results
    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Closing session
    session.close()
