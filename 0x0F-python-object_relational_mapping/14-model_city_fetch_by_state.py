#!/usr/bin/python3
""" class definition of a City """

import sys
from sqlalchemy.orm import Session
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    query_city = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id).order_by(City.id)
    for row in query_city:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
