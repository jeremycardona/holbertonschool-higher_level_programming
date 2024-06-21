#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from urllib.parse import quote_plus

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <mysql username> "
              "<mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = quote_plus(sys.argv[2])  # URL-encode the password
    dbname = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(f"{new_state.id}")

    session.close()
