# A-Frame Mobile AR Studio Prototype

This directory contains a simple A-Frame example that connects to the `ARServerExample.py` server.

## Usage

1. Start `ARStudioPrototype/ARServerExample.py`:

   ```bash
   python3 ARStudioPrototype/ARServerExample.py
   ```

2. Open `index.html` from this folder in a mobile browser (or desktop for testing). The page will periodically fetch tracking data from `http://localhost:5000/tracking` and apply it to a box entity.

3. Modify the server to stream real AR tracking data from ARKit or ARCore for a full experience.

This example demonstrates how A-Frame can be used as a lightweight web-based AR viewer that integrates with the Python server used for the Roblox plugin.
