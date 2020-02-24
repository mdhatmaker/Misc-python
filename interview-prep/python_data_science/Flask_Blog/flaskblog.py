from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# from python interpreter:
# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY'] = '7796427e61fbae200bdfd1efccd4f986'
# use SQLite for development (can change DB for production)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


# ---------------------------------------------------------
# Create classes for SQL Tables

# default table name is 'user'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# default table name is 'post'
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}'"
# ---------------------------------------------------------


# ---------------------------------------------------------
# To create database, change to project directory, launch
# python, and do the following:
# > from flaskblog import db
# > db.create_all()
# ---------------------------------------------------------
# > from flaskblog import User, Post
# > user_1 = User(username='Corey', email='C@demo.com', password='password')
# > db.session.add(user_1)
# > user_2 = User(username='JohnDoe', email='jd@demo.com', password='password')
# > db.session.add(user_2)
# > db.session.commit()
# ---------------------------------------------------------
# > User.query.all()
# > User.query.first()
# > User.query.filter_by(username='Corey').all()
# > user = User.query.filter_by(username='Corey').first()
# > user.id
# > user = user.query.get(1)
# > user.posts
# ---------------------------------------------------------
# > post_1 = Post(title='Blog 1', content='First post content!', user_id=user.id)
# > post_2 = Post(titel='Blog 2', content='Second post conent!', user_id=user.id)
# > db.session.add(post_1)
# > db.session.add(post_2)
# > db.session.commit()
# > user.posts
# > post = Post.query.first()
# > post
# > post.user_id
# > post.author
# ---------------------------------------------------------
# > db.drop_all()
# > db.create_all()
# ---------------------------------------------------------



# ---------------------------------------------------------
# before running:
# for mac/linux: export FLASK_APP=flaskblog.py
# for windows: set FLASK_APP=flaskblog.py
# then:
# for mac/linux: export FLASK_DEBUG=1
# for windows: set FLASK_DEBUG=1
# then:
# flask run (from the project directory)
# ---------------------------------------------------------


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    #return "<h1>Home Page<h1>"
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


# This avoids the need to set FLASK_DEBUG=1
# from cmd line: python flaskblog.py
if __name__ == "__main__":
    app.run(debug=True)


