from flask import Flask, render_template, url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime

import os
port = int(os.environ.get("PORT", 5000))

posts = [ {"author" : "henry", "date": "11th Jnauary","content" : "blah blah blah"}, { "author" : "james", "date": "4th Jamuary","content" : "blah blah blah"}]
app = Flask("__name__")
app.config['SECRET_KEY'] = "12345"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(20), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref='author', lazy=True)

    def __repr__(self):
        return 'User(%s,%s,%s) % (self.username, self.email, self.image_file)'

class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)



    def __repr__(self):
        return "Post('{%s}', '{%s}') % (self.title, self.date_posted)"



@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", title ="Home")

@app.route("/posts")
def display_posts():
    return render_template("posts.html", title= "Heroku web app", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register", methods=['GET', 'POST'])
def registration():
    form=RegistrationForm()
    if form.validate_on_submit():
        password=form.password.data
        user = User(username=form.user.data, email=form.email.data, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Account Created for %s !" % form.username.data, 'success')
        return redirect(url_for('index'))
    return render_template("register.html", title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@iii.com' and form.password.data == 'password':
            flash("You have been logged in!", 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful - Please check logins details', 'danger')

    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
