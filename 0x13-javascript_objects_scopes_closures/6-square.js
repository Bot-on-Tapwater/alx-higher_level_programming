#!/usr/bin/node

const ogSquare = require('./5-square');

class Square extends ogSquare {
  charPrint (c) {
    /* console.log('We printing in this bitch'); */
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(`${`${c}`.repeat(this.width)}`);
      }
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(`${'X'.repeat(this.width)}`);
      }
    }
  }
}

module.exports = Square;
