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
    query = "SELECT * FROM states ORDER BY id ASC"
    holder.execute(query)
    rows = holder.fetchall()
    for row in rows:
        print(row)
    holder.close()
    connection.close()
