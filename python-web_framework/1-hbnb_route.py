"""FLASK initialized"""
from flask import Flask

app = Flask(__name__)

"""create route at / display --> “Hello HBNB!”"""
@app.route('/',strict_slashes=False)
def hello():
    return "Hello HBNB!"

"""create route at /hbnb display --> “HBNB”"""
@app.route('/hbnb',strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == '__main__':
    '''run flask on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000)