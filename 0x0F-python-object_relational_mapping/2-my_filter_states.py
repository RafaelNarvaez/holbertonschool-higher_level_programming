#!/usr/bin/python3
""" Simple list of table states """

import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    holder = connection.cursor()
    query = "SELECT * FROM states\
    WHERE name='{}' ORDER BY id ASC".format(sys.argv[4])
    holder.execute(query)
    rows = holder.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    holder.close()
    connection.close()
