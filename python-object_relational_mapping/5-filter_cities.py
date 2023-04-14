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

    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id ASC", (sys.argv[4],))

    rows = cur.fetchall()

    print(", ".join([row[0] for row in rows[0:3]]))

    db.close()
