from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(
  app,
  resources={
    r"/api/*": {
        "origins": ['http://localhost:3000'],
    }
  },
  supports_credentials=True,
)

@app.route('/api/ping')
def ping():
    response = jsonify({'ping': 'pong'})
    response.set_cookie(
      key='token',
      value='example-token',
      domain='127.0.0.1',
      path='/'
    )
    return response
