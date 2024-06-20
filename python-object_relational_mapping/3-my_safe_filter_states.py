#!/usr/bin/python3
"""safe query from sql injections"""


import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> \
              <database name> <state name>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname,
        charset="utf8"
    )

    # Create a cursor object
    cursor = db.cursor()

    # Prepare SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with user input
    cursor.execute(query, (state_name,))

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()
