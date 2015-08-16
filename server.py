__author__ = 'TerraceBoiz'
import json

from functools import wraps
from flask import Flask, jsonify, request, Response
import state

app = Flask(__name__)


stateNow = state.State(1, 5, 6)

 
@app.route("/raspberry/pi/state", methods=['GET'])
def get_state():
    ret = json.dumps(stateNow.__dict__)
    return Response(ret, mimetype='application/json')

@app.route("/raspberry/pi/state", methods=['POST'])
def post_state():
    if not request.json:
        abort(400)
    global stateNow
    stateNow = state.State(request.json['id'], request.json['score1'], request.json['score2'])
    ret = json.dumps(stateNow.__dict__)
    return Response(ret, mimetype='application/json')

    
    
def main():
    while True:
        app.run(host='0.0.0.0', port=8080)
main()
