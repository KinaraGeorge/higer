#!/usr/bin/node
let arg = process.argv[2];
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
    while (count < arg) {
	console.log('C is fun');
	count++;
    }
}
