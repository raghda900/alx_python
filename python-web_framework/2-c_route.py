"""FLASK initialized"""
from flask import Flask
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


if __name__ == '__main__':
    '''run flask on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)