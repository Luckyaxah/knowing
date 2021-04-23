import random

from faker import Faker
from sqlalchemy.exc import IntegrityError

from knowing.extensions import db
from knowing.models import User

fake = Faker()

def fake_admin():
    user = User(
        name='admin',
        confirmed = True,
        username = 'admin',
        member_since = fake.date_this_decade(),
        email = fake.email()
    )
    user.set_password('123456')
    db.session.add(user)
    db.session.commit()

def fake_user(count=5):

    for i in range(count):
        user = User(
            name = fake.name(),
            confirmed = True,
            username = fake.user_name(),
            member_since = fake.date_this_decade(),
            email = fake.email()
        )
        user.set_password('123456')
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
