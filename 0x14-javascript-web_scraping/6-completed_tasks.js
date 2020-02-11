#!/usr/bin/node
const request = require('request');
const final = {};
const indiv;
request.get(process.argv[2], function (error, request, body) {
  if (error) {
    console.log(error);
  }
  if (request.statusCode === 200) {
    for (indiv of JSON.parse(body)) {
      if (indiv.completed === true) {
        if (final[indiv.userId] === undefined) {
          final[indiv.userId] = 0;
        }
        final[indiv.userId]++;
      }
    }
  }
  console.log(final);
});
