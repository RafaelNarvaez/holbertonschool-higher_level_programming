#!/usr/bin/python3
""" filter states by cities """
if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    num_rows = cursor.execute("""SELECT DISTINCT cities.name FROM cities
                                 JOIN states ON states.id = cities.state_id
                                 WHERE states.name = %s
                                 """, (sys.argv[4],))
    for r in range(num_rows):
        if (r == num_rows - 1):
            print(cursor.fetchone()[0], end="")
        else:
            print(cursor.fetchone()[0], end=", ")
    print()
    cursor.close()
    db.close()
