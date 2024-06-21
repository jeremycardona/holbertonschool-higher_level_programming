#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
The script takes 3 arguments: mysql username, mysql password and database name.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from urllib.parse import quote_plus

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./13-model_state_delete_a.py <mysql username> "
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

    # Query and delete all State objects with a name containing the letter 'a'
    states_to_delete = session.query(State).\
        filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction
    session.commit()

    # Close the session
    session.close()
