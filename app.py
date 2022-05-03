from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/api/*": {
        "origins": ['http://localhost:3000'],
    }
})

@app.route('/api/ping')
def ping():
    response = jsonify({'ping': 'pong'})
    response.set_cookie('token', 'example-token')
    return response
