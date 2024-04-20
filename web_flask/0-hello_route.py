#!/usr/bin/python3
"""
Script to start a Flask web application.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route to display "Hello HBNB!".
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    """The main function"""
    app.run(host='0.0.0.0', port=5000)
