#!/usr/bin/python3
"""List all City objects"""

if __name__ == '__main__':

    import sys
    from sqlalchemy.orm import sessionmaker
    from model_state import State
    from model_city import City
    from sqlalchemy import create_engine

    USR = sys.argv[1]
    PWD = sys.argv[2]
    DB = sys.argv[3]
    HST = 'localhost'
    PRT = '3306'

    connection_url = f"mysql://{USR}:{PWD}@{HST}:{PRT}/{DB}"

    """Engine to connect to DB"""
    engine = create_engine(connection_url)

    """Session class for session objects"""
    Session = sessionmaker(bind=engine)

    """Session with database started"""
    session = Session()

    """Sample query"""
    qry = session.query(State, City).filter(State.id == City.state_id).\
        order_by(City.id.asc()).all()

    """Iterateing through results of query"""
    for state, city in qry:
        print(f"{state.name}: ({state.id}) {city.name}")
