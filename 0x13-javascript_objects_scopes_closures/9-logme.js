#!/usr/bin/node
global.n = 0;
exports.logMe = function (item) {
  console.log(global.n + ': ' + item);
  global.n++;
};
