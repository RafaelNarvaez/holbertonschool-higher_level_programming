#!/usr/bin/python3
""" Create file that contains the class definition of City
    and a instance of Base = declaratibe_base() with relationship
"""
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()


class City (Base):
    """ Model City define a city object with relationship
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
