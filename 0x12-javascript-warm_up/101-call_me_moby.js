#!/usr/bin/node
exports.callMeMoby = function (a, b) {
  for (let j = 0; j < a; j++) {
    b();
  }
};
