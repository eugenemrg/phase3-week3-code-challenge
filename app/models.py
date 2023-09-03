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
    
    @classmethod
    def reviews(cls):
        #  returns a collection of all the reviews for the `Restaurant`
        pass
    
    def customers(cls):
        # returns a collection of all the customers who reviewed the `Restaurant`
        pass

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
            
    def reviews(self):
        # should return a collection of all the reviews that the `Customer` has left
        pass
    
    def restaurants(self):
        # should return a collection of all the restaurants that the `Customer` has reviewed
        pass
    
    def full_name(self):
        # returns the full name of the customer, with the first name and the last name  concatenated, Western style.
        return f'{self.first_name} {self.last_name}'
    
    def favorite_restaurant(self):
        # returns the restaurant instance that has the highest star rating from this customer
        pass
    
    def add_review(self, restaurant, rating):
        # takes a `restaurant` (an instance of the `Restaurant` class) and a rating
        # creates a new review for the restaurant with the given `restaurant_id`
        pass
    
    def delete_reviews(self, restaurant):
        # takes a `restaurant` (an instance of the `Restaurant` class) and
        # removes **all** their reviews for this restaurant
        # you will have to delete rows from the `reviews` table to get this to work!
        pass
        

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
    
    def customer(self):
        # should return the `Customer` instance for this review
        pass
    
    def  restaurant(self):
        # should return the `Restaurant` instance for this review
        pass
    
    def full_review(self):
        c = self.customer()
        r = self.restaurant()
        return f'Review for {r.name} by {c.full_name()}: {self.star_rating} stars.'