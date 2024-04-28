#!/usr/bin/python3
"""A script that lists all states with names starting with uppecase N from the database hbtn_0e_0_usa"""
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
    cur.execute("SELECT * FROM states \
            WHERE name LIKE 'N%' COLLATE utf8mb4_bin \
                ORDER BY id ASC")
    """Obtaining Query Results"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
