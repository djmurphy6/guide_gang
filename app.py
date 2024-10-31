# app.py
import flask 
from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
@app.route("/index")
def index():
    """The main page of the application"""
    return flask.render_template("index.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)