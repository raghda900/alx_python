"""FLASK initialized"""
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

"""create route at / display --> “Hello HBNB!”"""
@app.route('/',strict_slashes=False)
def hello():
    return "Hello HBNB!"

"""create route at /hbnb display --> “HBNB”"""
@app.route('/hbnb',strict_slashes=False)
def hbnb():
    return "HBNB"

"""create route at /c/<text> display -->  “C ” followed by the value of the text """
@app.route('/c/<text>',strict_slashes=False)
def c(text):
    text=text.replace('_', ' ',)
    return f"C {escape(text)}"

"""create route at /python/<text> display -->  “python ” followed by the value of the text defult 'is cool' """
@app.route('/python/<text>',strict_slashes=False)
@app.route('/python',strict_slashes=False)
def python(text="is cool"):
    text=text.replace('_', ' ',)
    return f"Python {escape(text)}"

"""create route at /number/<n> display --> “n is a number” if n is a number"""
@app.route('/number/<int:n>',strict_slashes=False)
def number(n):
    return f"{escape(n)} is a number"

"""create route at /number_template/<n> render html """
@app.route('/number_template/<int:n>',strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', num=n)

if __name__ == '__main__':
    '''run flask on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)