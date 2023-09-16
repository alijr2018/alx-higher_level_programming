#!/usr/bin/bash

"""
 script that takes in an argument and displays all values in the states
  table of hbtn_0e_0_usa where name matches the argument.
 """

import MySQLdb
import sys

# Retrieve command line arguments
username, password, database, state_name = sys.argv[1],
sys.argv[2], sys.argv[3], sys.argv[4]

# Connect to MySQL server
try:
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # Execute the query to retrieve states matching the provided name
    cursor.execute(
        "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC",
        (state_name,)
    )

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print(f"An error occurred: {e}")
