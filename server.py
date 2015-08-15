__author__ = 'Mark'
import json

from flask import Flask, jsonify, request
import state

app = Flask(__name__)


stateNow = state.State(1, 5, 6)

def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator
 
 
def editHeaders(f):
    return add_response_headers({'Content-Type': "application/json"})(f)
    
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


@app.route("/raspberry/pi/state")
@editHeaders
def headers_edited():
    return "Headers Updated"
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
