#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

try:
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

except MySQLdb.Error as e:
    print(f"An error occurred: {e}")
