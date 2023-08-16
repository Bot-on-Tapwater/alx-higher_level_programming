#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /* console.log('Testing out print'); */
    for (let i = 0; i < this.height; i++) {
      console.log(`${'X'.repeat(this.width)}`);
    }
  }

  rotate () {
    const tempWidth = this.width;

    this.width = this.height;
    this.height = tempWidth;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}

module.exports = Rectangle;
