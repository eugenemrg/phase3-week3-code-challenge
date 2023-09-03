from sqlalchemy import create_engine
from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///reviewer.db')

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    price = Column(Integer())
    
    def __repr__(self):
        return f"Restaurant {self.id}: " \
            + f"{self.name}, " \
            + f"Price {self.price}"

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String(), index=True)
    
    def __repr__(self):
        return f"Customer {self.id}: " \
            + f"{self.first_name} " \
            + f"{self.last_name}"