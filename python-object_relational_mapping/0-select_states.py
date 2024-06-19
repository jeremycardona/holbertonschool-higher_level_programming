#!/usr/bin/python3
import sys
import MySQLdb

def list_states(username, password, dbname):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    # Fetch all the results
    states = cursor.fetchall()
    
    # Print the results
    for state in states:
        print(state)
    
    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
    # Call the function to list states
    list_states(username, password, dbname)
