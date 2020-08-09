#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    statename = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    cursor = db.cursor()
    cursor.execute("""SELECT
                    cities.name
                    FROM cities INNER JOIN states
                    ON cities.state_id=states.id
                    WHERE states.name=%s""", (statename,))
    rows = cursor.fetchall()
    for row in rows:
        for col in row:
            print(col, end='')
        if rows.index(row) < len(rows) - 1:
            print(end=', ')
        else:
            print()

    cursor.close()
    db.close()
