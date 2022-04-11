#!/usr/bin/python3
""" Simple list of table states """

import sys
import MySQLdb


def main():
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    holder = connection.cursor()
    userInput = sys.argv[4]
    holder.execute("""SELECT id,name FROM states WHERE name = %s
            ORDER by id ASC""", (userInput,))
    rows = holder.fetchall()
    for row in rows:
        print(row)
    holder.close()
    connection.close()


if __name__ == "__main__":
    main()
© 2022 GitHub, Inc.
Terms
Privacy
import sys
import MySQLdb


def main():
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    holder = connection.cursor()
    userInput = sys.argv[4]
    holder.execute("""SELECT id,name FROM states WHERE name = %s
            ORDER by id ASC""", (userInput,))
    rows = holder.fetchall()
    for row in rows:
        print(row)
    holder.close()
    connection.close()


if __name__ == "__main__":
    main()
