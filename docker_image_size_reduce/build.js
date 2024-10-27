// build.js
const fs = require('fs');
const path = require('path');

// Define the source and destination paths
const source = path.join(__dirname, 'app.js');
const destination = path.join(__dirname, 'dist', 'app.js');

// Create the dist directory if it doesn't exist
fs.mkdirSync(path.join(__dirname, 'dist'), { recursive: true });

// Copy the file
fs.copyFileSync(source, destination);

console.log('Build completed: app.js has been copied to dist/app.js');
