#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(sys.argv[0]))
    sys.exit(1)

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

try:
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows and print them
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))
    sys.exit(1)
