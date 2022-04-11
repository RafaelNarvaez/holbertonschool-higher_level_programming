#!/usr/bin/python3
""" script that creates the State “California” with
    the City “San Francisco” from the
    database hbtn_0e_100_usa: (100-relationship_states_cities.py)
    with sqlalchemy
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    new_state = State(name='California')
    new_state.cities.append(City(name='San Francisco'))
    session.add(new_state)
    session.commit()
    session.close()
