const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const QRCode = require('qrcode');

const app = express();
const uploadsDir = path.join(__dirname, 'uploads');
fs.mkdirSync(uploadsDir, { recursive: true });
const upload = multer({ dest: uploadsDir });

app.use(express.static(path.join(__dirname, 'public')));

app.post('/upload-beat', upload.single('beat'), (req, res) => {
  if (!req.file) {
    return res.status(400).send('No file uploaded');
  }
  res.json({ file: req.file.filename });
});

app.get('/qr', (req, res) => {
  const url = req.query.url || '';
  if (!url) {
    return res.status(400).send('Missing url');
  }
  QRCode.toDataURL(url, (err, dataUrl) => {
    if (err) return res.status(500).send('QR generation failed');
    res.type('text/plain').send(dataUrl);
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
