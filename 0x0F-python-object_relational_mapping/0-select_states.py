#!/usr/bin/python3
import MySQLdb
import sys

if len(sys.argv) != 4:
    sys.exit(1)

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

try:
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print("MySQL Error: {}".format(e))
    sys.exit(1)
