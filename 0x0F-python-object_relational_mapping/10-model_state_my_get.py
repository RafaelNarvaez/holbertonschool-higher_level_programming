#!/usr/bin/python3
""" search for states """

import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    states = (session.query(State).filter(State.name == sys.argv[4])
              .order_by(State.id))
    found = 0
    for state in states:
        found += 1
        print("{}".format(state.id, state.name))
    if found == 0:
        print("Not found")

    session.close()
