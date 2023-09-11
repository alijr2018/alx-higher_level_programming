#!/usr/bin/node

const arg = process.argv.slice(2).map(Number);

if (arg.length < 2) {
  console.log(0);
} else {
  const sortedArg = arg.sort((a, b) => b - a);
  console.log(sortedArg[0]);
}
