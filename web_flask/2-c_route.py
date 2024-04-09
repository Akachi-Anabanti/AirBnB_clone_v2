#!/usr/bin/python3
"""A Simple flask app that serves a text"""
from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
