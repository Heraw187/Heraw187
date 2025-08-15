"""Utility to send sample tracking data to the AR server.

Run this script after starting ``ARServerExample.py`` to simulate an
AR device pushing pose data. The server stores the latest payload and the
Roblox plugin can then fetch it.
"""

import json
import requests

URL = "http://localhost:5000/tracking"

payload = {
    "position": {"x": 1, "y": 2, "z": 3},
    "rotation": {"x": 10, "y": 20, "z": 30},
}

resp = requests.post(URL, json=payload)
resp.raise_for_status()
print("Sent payload:", json.dumps(payload))

# Fetch it back to verify
verify = requests.get(URL)
print("Server returned:", verify.json())
