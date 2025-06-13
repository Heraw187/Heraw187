# Welcome

This repository contains experiments and prototypes. See `ARStudioPrototype/` for a simple example of integrating augmented reality with Roblox Studio.

## Web Audio Recorder Prototype

The `web/` folder contains a small Node.js app that provides an audio recorder and beat uploader interface. Run it locally with:

```bash
cd web
npm install
npm start
```

The app serves `http://localhost:3000` where you can record vocals, upload an MP3 beat, and generate QR codes for sharing links. Uploads are stored in `web/uploads` which the server creates automatically. To create a QR code for a link, open `/qr?url=YOUR_URL` in the browser.
