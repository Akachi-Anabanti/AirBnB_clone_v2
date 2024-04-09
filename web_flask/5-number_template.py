#!/usr/bin/python3
"""A Simple flask app that serves a text"""
from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def home():
    """Home Page"""
    return("HBNB!")


@app.route("/hbnb")
def hbnb():
    """Hbnb Page"""
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def show_text(text):
    """shows the text"""
    return "C" + " " + escape(text).replace("_", " ")


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """Show python text"""
    return "Python" + " " + escape(text).replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Displays int variable"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def template_route(n):
    """renders a template"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
