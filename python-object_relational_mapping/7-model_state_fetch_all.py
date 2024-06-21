#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from urllib.parse import quote_plus

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = quote_plus(sys.argv[2])  # URL-encode the password
    dbname = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}', pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
