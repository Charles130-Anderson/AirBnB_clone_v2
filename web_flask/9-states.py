#!/usr/bin/python3
"""Starts a Flask web application."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the current SQLAlchemy Session."""
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states():
    """Displays a HTML page with a list of all State objects."""
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def display_state_by_id(id):
    """Displays a HTML page with a list of City objects linked to the State."""
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=None, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
