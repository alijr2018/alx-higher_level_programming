#!/usr/bin/node

const fs = require('fs');

const File1 = fs.readFileSync(process.argv[2], 'utf8');
const File2 = fs.readFileSync(process.argv[3], 'utf8');
const Filedest = process.argv[4];

fs.writeFileSync(Filedest, File1 + File2);
