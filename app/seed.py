#!/home/eugene/.pyenv/shims python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Customer, Restaurant, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///reviewer.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Customer).delete()
    session.query(Restaurant).delete()
    session.query(Review).delete()

    fake = Faker()

    customers = []
    for i in range(50):
        customer = Customer(
            first_name=fake.first_name(),
            last_name=fake.last_name()
        )

        # add and commit individually to get IDs back
        session.add(customer)
        session.commit()

        customers.append(customer)


    restaurants = []
    for i in range(25):
        restaurant = Restaurant(
            name=fake.city(),
            price= random.randint(450, 3000)
        )

        session.add(restaurant)
        session.commit()

        restaurants.append(restaurant)


    reviews = []
    for customer in customers:
        for i in range(random.randint(1,3)):
            restaurant = random.choice(restaurants)
            
            review = Review(
                star_rating=random.randint(0, 5),
                restaurant_id=restaurant.id,
                customer_id=customer.id
            )

            session.add(review)
            session.commit()
            reviews.append(review)
            
    session.close()