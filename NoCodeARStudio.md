# Building a No-Code AR Studio with Frsmey and WebAR

This guide outlines a conceptual approach for assembling a simple AR authoring environment without writing code. The flow assumes you are using **Frsmey** (a drag-and-drop tool for layouts) together with a WebAR framework.

## 1. Design the AR Scene in Frsmey

1. Create a new project in Frsmey.
2. Use its interface to place 3D models, images, and UI elements.
3. Configure interactions or animations using built-in settings—no scripting required.

## 2. Export to WebAR

1. Frsmey lets you export your scene as HTML/CSS/JS files.
2. Choose an export format compatible with WebAR platforms such as **AR.js** or **8th Wall**.
3. Download the exported files to your computer.

## 3. Host and Test

1. Deploy the exported package to a web server (GitHub Pages or similar).
2. Open the link on a mobile device with camera access.
3. Your scene should load in the browser and display the AR content.

## 4. Optional Integration with Roblox

If you want to connect WebAR output back to Roblox (as in the prototype under `ARStudioPrototype/`), you can:

1. Run the example AR server from `ARStudioPrototype/ARServerExample.py`.
2. Adjust the Roblox plugin to fetch data from your WebAR app if it exposes tracking information.

This approach keeps the workflow entirely no-code while leveraging Frsmey for layout and WebAR for deployment.
