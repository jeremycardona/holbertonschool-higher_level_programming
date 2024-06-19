#!/usr/bin/python3
"""query for all states"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8") 
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
