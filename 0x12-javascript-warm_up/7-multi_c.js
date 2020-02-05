#!/usr/bin/node
//  prints x times C is fun

const integer = parseInt(process.argv[2]);

if (integer) {
  for (let i = 0; i < integer; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
