#!/usr/bin/python3

"""
A script that takes in the name of a state as an argument and lists,
all cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    row = cur.fetchall()
    k = []
    for j in row:
        k.append(j[1])
    print(", ".join(k))

    cur.close()
    db.close()
