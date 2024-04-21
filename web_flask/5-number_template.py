#!/usr/bin/python3
"""Start web application with two routings
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Display 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """Display 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>')
def display_c(text):
    """Display 'C' followed by the value of the text variable."""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def display_python(text='is cool'):
    """Display 'Python' followed by the value of the text variable."""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def is_number(n):
    """Display 'n is a number' only if n is an integer."""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieve template for request."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
