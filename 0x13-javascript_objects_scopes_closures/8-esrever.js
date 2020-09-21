#!/usr/bin/node
exports.esrever = function (list) {
  const rl = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rl.push(list[i]);
  }
  return rl;
};
