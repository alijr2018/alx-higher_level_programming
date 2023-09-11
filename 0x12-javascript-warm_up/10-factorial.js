#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return (1);
  } else if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const fac = parseInt(process.argv[2]);
const res = factorial(fac);
console.log(res);
