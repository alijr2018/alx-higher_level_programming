#!/usr/bin/node

const fs = require('fs');
const sourceFile1 = process.argv[2];
const sourceFile2 = process.argv[3];
const destinationFile = process.argv[4];

if (!sourceFile1 || !sourceFile2 || !destinationFile) {
  console.error('Usage: ./102-concat.js <sourceFile1> <sourceFile2> <destinationFile>');
  process.exit(1);
}

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) {
    console.error(err.message);
    process.exit(1);
  }

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) {
      console.error(err.message);
      process.exit(1);
    }

    const concatenatedData = data1 + '\n' + data2;

    fs.writeFile(destinationFile, concatenatedData, 'utf8', (err) => {
      if (err) {
        console.error(err.message);
        process.exit(1);
      }

      console.log('Concatenation complete.');
    });
  });
});
