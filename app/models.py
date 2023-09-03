from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

engine = create_engine('sqlite:///reviewer.db')

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String(), index=True)
    price = Column(Integer())
    
    reviews = relationship('Review', back_populates='restaurant')
    users = association_proxy('reviews', 'customer', creator=lambda cust: Review(customer=cust))
    
    def __repr__(self):
        return f"Restaurant {self.id}: " \
            + f"{self.name}, " \
            + f"Price {self.price}"

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(), index=True)
    last_name = Column(String(), index=True)
    
    reviews = relationship('Review', back_populates='customer')
    restaurants = association_proxy('reviews', 'restaurant', creator=lambda res: Review(restaurant=res))
    
    def __repr__(self):
        return f"Customer {self.id}: " \
            + f"{self.first_name} " \
            + f"{self.last_name}"

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    
    customer = relationship('Customer', back_populates='reviews')
    restaurant = relationship('Restaurant', back_populates='reviews')

    def __repr__(self):
        return f'Review(id={self.id}, ' + \
            f'star rating={self.star_rating}, ' + \
            f'restaurant id={self.restaurant_id}, ' + \
            f'customer id={self.customer_id})'