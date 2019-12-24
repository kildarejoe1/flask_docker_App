from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm

import os
port = int(os.environ.get("PORT", 5000))

posts = [ {"author" : "henry", "date": "11th Jnauary","content" : "blah blah blah"}, { "author" : "james", "date": "4th Jamuary","content" : "blah blah blah"}]
app = Flask("__name__")
app.config['SECRET_KEY'] = "12345"


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
