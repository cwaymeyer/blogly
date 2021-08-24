"""Seed file to make sample data for users db"""

from models import User, Post, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Empty table
User.query.delete()
Post.query.delete()

# Users
john = User(first_name='John', last_name='Williams', image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Andrzej_Person_Kancelaria_Senatu.jpg/1200px-Andrzej_Person_Kancelaria_Senatu.jpg')
bob = User(first_name='Bob', last_name='Watson', image_url='https://www.lynxwebdevelopment.co.uk/lgd-callanish/wp-content/uploads/2020/07/Pierre-Person-1080x1080.jpg')
phil = User(first_name='Phil', last_name='Jefferson')

db.session.add(john)
db.session.add(bob)
db.session.add(phil)

db.session.commit()

# Posts
first = Post(title = 'First Post', content='Content here!', user_id='1')
second = Post(title = 'Some more thoughts', content='Theres not really much more to say', user_id='2')

db.session.add(first)
db.session.add(second)

db.session.commit()