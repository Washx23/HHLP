#!/usr/bin/python3
"""SQL start"""


import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name)

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
            FROM cities \
            JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    db.close()
