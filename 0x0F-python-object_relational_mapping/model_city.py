#!/usr/bin/python3
"""Class City"""

# model_city.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import State

Base = declarative_base()


class City(Base):
    """Class City"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(length=128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    """state = relationship("State", back_populates="cities")"""


"""State.cities = relationship("City", back_populates='state')"""
