#!/usr/bin/python3
"""List all states starting with N"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    MY_HOST = 'localhost'
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    state_name = sys.argv[4]

    """Establish connection to DB"""
    db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)

    """Create cursor object"""
    cur = db.cursor()

    qry = "SELECT * \
        FROM states WHERE states.name = '{}' ORDER BY \
            states.id ASC;".format(state_name)

    cur.execute(qry)

    """Capture all rows returned by query"""
    rows = cur.fetchall()

    for state in rows:
        print(state)
