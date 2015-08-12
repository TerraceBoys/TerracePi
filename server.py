__author__ = 'Mark'

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Fuck!"


def main():
    app.run(host='0.0.0.0', port=8080)

