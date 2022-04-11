#!/usr/bin/python3
""" filter states by cities """
import sys
import MySQLdb


def main():
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        )
    state_name = sys.argv[4]
    holder = connection.cursor()
    holder.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (state_name,))
    rows = holder.fetchall()
    auxvar = ""
    for row in rows:
        auxvar += row[0] + ", "
    print(auxvar[0:-2:])
    holder.close()
    connection.close()


if __name__ == "__main__":
    main()
