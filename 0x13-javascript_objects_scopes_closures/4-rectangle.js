#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let x = '';
    for (let i = 0; i < this.width; i++) {
	x += 'X';
    }

    for (let j = 0; j < this.height; j++) {
	console.log(x);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    let x, y;
    x = this.width * 2;
    y = this.height * 2;
    this.width = x;
    this.height = y;
  }
}

module.exports = Rectangle;
