#!/usr/bin/node
const SquareDef = require('./5-square.js');
module.exports = class Square extends SquareDef {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let linePrint = '';
      for (let i = 0; i < this.width; i++) {
        linePrint += c;
      }
      for (let j = 0; j < this.height; j++) {
        console.log(linePrint);
      }
    }
  }
};
