#!/usr/bin/python3
"""
module 1-hello_route
Starts a Flask Web application listening on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """Displays a greeting"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays a greeting"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
