#!/usr/bin/node

const i = parseInt(process.argv[2]);

if (isNaN(i) || i <= 0) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < i; j++) {
    console.log('C is fun');
  }
}
