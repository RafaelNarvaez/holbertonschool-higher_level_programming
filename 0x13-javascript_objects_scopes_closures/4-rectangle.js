#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let stringLine = '';
    for (let i = 0; i < this.width; i++) {
      stringLine += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(stringLine);
    }
  }

  rotate () {
    const varSwap = this.height;
    this.height = this.width;
    this.width = varSwap;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
