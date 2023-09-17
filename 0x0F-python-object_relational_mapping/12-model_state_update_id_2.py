#!/usr/bin/python3

"""
A script that changes the name of a State object from,
the database hbtn_0e_6_usa.
"""

from sys import argv
from model_state import Base
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    state_add = session.query(State).filter(State.name == 'Louisiana').one()
    print(state_add.id)

    session.close()
