#!/usr/bin/node

function callMeMoby (x, y) {
  for (let j = 0; j < x; j++) {
    y();
  }
}

module.exports = {
  callMeMoby
};
