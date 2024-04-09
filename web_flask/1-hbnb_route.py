#!/usr/bin/python3
"""A Simple flask app that serves a text"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    """Home Page"""
    return("HBNB!")


@app.route("/hbnb")
def hbnb():
    """Hbnb Page"""
    return("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
