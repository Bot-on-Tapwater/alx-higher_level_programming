#!/usr/bin/node

const arg = process.argv[2];

if (Number.isInteger(Number(arg))) {
  console.log(`${parseInt(arg)}`);
} else {
  console.log('Not a number');
}
