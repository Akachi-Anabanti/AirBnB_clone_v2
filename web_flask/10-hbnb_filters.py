#!/usr/bin/python3
"""A flask application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Defines page filters"""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)



@app.teardown_appcontext
def teardown(exc):
    """tear down"""
    storage.close()


if __name__ == "__main__":
    app.run(host="192.168.33.10")

