#!/usr/bin/node

const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
  /* console.log(`My number: ${parseInt(arg)}`); */
  const numLoop = parseInt(arg);
  for (let i = 0; i < numLoop; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
