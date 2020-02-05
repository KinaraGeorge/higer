#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
    for (let count = 0; count < arg; count++) {
	console.log('C is fun');
    }
}
