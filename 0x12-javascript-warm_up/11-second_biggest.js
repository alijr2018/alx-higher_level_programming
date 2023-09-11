#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b.slice(0, 2) - a.slice(0, 2));
  console.log(sortedArgs[1]);
}
