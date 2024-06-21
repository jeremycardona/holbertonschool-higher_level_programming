#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
The script takes 3 arguments: mysql username, mysql password and database name.
It changes the name of the State where id = 2 to "New Mexico".
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from urllib.parse import quote_plus

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./12-model_state_update_id_2.py <mysql username> "
              "<mysql password> <database name>")
        sys.exit(1)

    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = quote_plus(sys.argv[2])  # URL-encode the password
    dbname = sys.argv[3]

    # Create an SQLAlchemy engine for the MySQL database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Change the name of the state to "New Mexico"
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
