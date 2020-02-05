#!/usr/bin/node

function Factorials (number) {
  if (isNaN(number) || number === 1) {
    return 1;
  }
  return number * Factorials(number - 1);
}

console.log(Factorials(process.argv[2]));
