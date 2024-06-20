#!/usr/bin/python3
"""Start link class to table in database 
"""

import sys
from urllib.parse import quote_plus
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./6-model_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    username = sys.argv[1]
    password = quote_plus(sys.argv[2])  # URL-encode the password
    dbname = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)
    Base.metadata.create_all(engine)
