#!/usr/bin/node

const a = process.argv[2];

function convNum (num) {
  /* console.log('Converting to Integer'); */
  const number = parseInt(num);
  return (number);
}

function factorial (num) {
  const number = convNum(num);

  if (isNaN(number)) {
    return (1);
  } else if (number > 0) {
    return (number * factorial(number - 1));
  } else {
    return (1);
  }
}

console.log(`${factorial(a)}`);
