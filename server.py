__author__ = 'Mark'
import json

from flask import Flask, jsonify, request
import state

app = Flask(__name__)


stateNow = state.State(1, 5, 6)

@app.route("/raspberry/pi/state", methods=['GET'])
def get_state():
    return json.dumps(stateNow.__dict__)        

@app.route("/raspberry/pi/state", methods=['POST'])
def post_state():
    if not request.json:
        abort(400)
    global stateNow
    stateNow = state.State(request.json['id'], request.json['score1'], request.json['score2'])
    return json.dumps(stateNow.__dict__) 

def main():
    app.run(host='0.0.0.0', port=8080)
