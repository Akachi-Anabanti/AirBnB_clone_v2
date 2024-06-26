#!/usr/bin/python3
"""A FLASK APP"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """List the states
    Sorted by name"""

    states = storage.all(State)

    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLALchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
