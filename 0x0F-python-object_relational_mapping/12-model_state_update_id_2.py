#!/usr/bin/python3
"""Update state object"""

if __name__ == '__main__':

    import sqlalchemy
    from sqlalchemy import create_engine,\
        Column, Integer, UniqueConstraint, String
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    import sys
    from sqlalchemy.orm import sessionmaker

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

    # """New state"""
    # new_state = State(name='Louisiana')

    # """Add new state"""
    # session.add(new_state)

    """Query state to update"""
    states = session.query(State).filter(State.id == '2').first()

    """Update the state"""
    states.name = 'New Mexico'

    """Commit changes to DB"""
    session.commit()
