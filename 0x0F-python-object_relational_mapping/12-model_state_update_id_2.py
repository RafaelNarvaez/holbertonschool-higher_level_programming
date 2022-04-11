#!/usr/bin/python3
""" Update a State """

import sys
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state_update = session.query(State).filter_by(id=2).first()
    state_update.name = 'New Mexico'
    session.commit()
    session.close()
