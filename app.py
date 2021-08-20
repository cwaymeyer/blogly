"""Blogly application"""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = 'col3'
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


# SHOW USERS
@app.route('/')
def home():
    '''Redirect to users'''

    return redirect('/users')


@app.route('/users')
def users():
    '''List all users'''

    users = User.query.all()

    return render_template('users.html', users=users)


# CREATE USER
@app.route('/users/new')
def new_user():
    '''Create new user'''

    return render_template('/new-user.html')


@app.route('/users/new', methods=['POST'])
def submit_created_user():
    '''Submit new user data'''

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    avatar = request.form['url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=avatar)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')


# VIEW USER
@app.route('/users/<int:user_id>')
def user_details(user_id):
    '''View user details'''
    
    user = User.query.get_or_404(user_id)

    return render_template('user-details.html', user=user)


# EDIT USER
@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    '''Edit user data'''

    user = User.query.get_or_404(user_id)

    return render_template('edit-user.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def submit_edited_user(user_id):
    '''Submit edited user data'''

    user = User.query.get_or_404(user_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image_url = request.form['url']

    db.session.add(user)
    db.session.commit()

    return redirect('/users')


#  DELETE USER
@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    '''Delete user from database'''

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')



