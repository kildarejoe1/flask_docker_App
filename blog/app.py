from flask import Flask
port = int(os.environ.get("PORT", 5000))


app = Flask("__name__")


@app.route("/")
def index():
    return "<html> <title> Blog app </title> <body> Welcome to this flask app </body></html>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
