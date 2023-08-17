#!/usr/bin/python3
"""List all cities in a specific state"""

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

    qry = "SELECT cities.name\
        FROM cities JOIN states\
            ON states.id = cities.state_id\
                WHERE states.name = %s ORDER BY cities.id ASC;"

    cur.execute(qry, (state_name,))

    """Capture all rows returned by query"""
    rows = cur.fetchall()

    listStates = []
    for state in rows:
        for tup in state:
            listStates.append(tup)

    strStates = (", ").join(listStates)
    print(strStates)
