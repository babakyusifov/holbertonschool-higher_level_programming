#!/usr/bin/python3
"""Module"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State
from sys import argv

if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = (
        session.query(State, City)
        .join(City, State.id == City.state_id)
        .order_by(City.id)
        .all())

    for state, city in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    if session:
        session.close()
