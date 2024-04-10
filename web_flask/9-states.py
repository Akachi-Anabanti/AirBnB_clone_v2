#!/usr/bin/python3
"""A FLASK APP"""
from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy import select


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def all_states(id=None):
    """List the states
    Sorted by name"""
    states = storage.all(State)
    if id:
        for state in states.values():
            if state.id == id:
                # assign the state to states
                states = state
                return render_template("9-states.html", state=states)
        # return an empty template if no state is found
        return render_template("9-states.html")
    # return all states if the id is not given
    return render_template("9-states.html", state=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLALchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
