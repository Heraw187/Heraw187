"""Simple AR server example.

This script accepts AR tracking data via HTTP and serves the latest
reading to clients (e.g., the Roblox plugin).

POST JSON to ``/tracking`` with the fields ``position`` and ``rotation``
to update the stored data. ``GET /tracking`` returns the most recent
reading. This allows a mobile AR app to stream tracking data that the
Roblox plugin can consume.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory store for the most recent tracking data
latest_data = {
    "position": {"x": 0, "y": 0, "z": 0},
    "rotation": {"x": 0, "y": 0, "z": 0},
}


@app.route("/tracking", methods=["GET", "POST"])
def tracking():
    """GET returns the latest data, POST updates it."""
    global latest_data
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        if "position" in data and "rotation" in data:
            latest_data = data
            return ("", 204)
        return jsonify({"error": "Invalid data"}), 400
    return jsonify(latest_data)


if __name__ == "__main__":
    # Listen on all interfaces so mobile devices on the same network can connect
    app.run(host="0.0.0.0", port=5000)
