#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    """create a cursor object"""
    cur = db.cursor()
    """The execute function requires one parameter, the query."""
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states\
            ON cities.state_id=states.id")
    """obtaining query results"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
