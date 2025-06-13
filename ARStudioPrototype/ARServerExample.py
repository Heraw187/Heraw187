"""Simple AR server example.
This script simulates AR tracking data for testing the Roblox plugin.
"""
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/tracking')
def tracking():
    data = {
        "position": {"x": 0, "y": 5, "z": 0},
        "rotation": {"x": 0, "y": 0, "z": 0},
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=5000)
