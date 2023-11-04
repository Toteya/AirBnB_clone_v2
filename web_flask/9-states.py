#!/usr/bin/python3
"""
Runs a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception=None):
    """Removes/closes the current SQLAlchemy session
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    """Display States HTML page"""
    states = storage.all(State).values()
    close_session()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def state(id=None):
    """Display States HTML page"""
    key = "State.{}".format(id)
    state = storage.all(State).get(key, None)
    close_session()
    return render_template('9-states.html', state=state, id=id)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
