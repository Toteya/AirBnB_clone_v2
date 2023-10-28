#!/usr/bin/python3
"""
module 5-number_template
Starts a Flask Web application listening on 0.0.0.0:5000
"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """Displays a greeting"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays a greeting"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Display C followed by text"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """Display Python followed by text"""
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>")
def number(n):
    """ Checks if n is a number """
    return f"{escape(n)} is a number"


@app.route("/number_template/<int:n>")
def number_template(n):
    """Displays an HTML page only if n is a number"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
