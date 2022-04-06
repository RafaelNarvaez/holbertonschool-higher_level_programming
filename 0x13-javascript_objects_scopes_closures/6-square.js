#!/usr/bin/node
const square = require('./5-square');
/**
 * Represent a Square
 * @extends square
 */
class Square extends square {
  /** Print with c character */
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
