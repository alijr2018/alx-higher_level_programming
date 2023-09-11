#!/usr/bin/node

const fac = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n) || n < 0) {
    return (1);
  } else if (n === 0) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}
const res = factorial(fac);
console.log(res);
