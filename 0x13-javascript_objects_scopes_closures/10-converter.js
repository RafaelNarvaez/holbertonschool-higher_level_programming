#!/usr/bin/node
exports.converter = function (base) {
  function changeBase (n) {
    return n.toString(base);
  }
  return changeBase;
};
