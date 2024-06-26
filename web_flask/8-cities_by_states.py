#!/usr/bin/python3
"""A FLask application"""
from flask import Flask, render_template
from models import storage
import os

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def city_by_state():
    """Get cities by the State"""
    states = storage.all("State")
    states = states.values()
    return render_template("8-cities_by_states.html",
                           states=states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
