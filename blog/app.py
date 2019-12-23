from flask import Flask, render_template

import os
port = int(os.environ.get("PORT", 5000))

posts = [ {"author" : "henry", "date": "11th Jnauary"}, { "author" : "james", "date": "4th Jamuary"}]
app = Flask("__name__")


@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/posts")
def display_posts():
    return render_template("posts.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
