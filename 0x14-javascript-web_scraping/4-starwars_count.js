#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  let count = 0;
  if (err) {
    console.log(err);
  }
  for (const movie of JSON.parse(body).results) {
    for (const character of movie.characters) {
      if (character.includes(String('/18/'))) {
        count++;
      }
    }
  }
  console.log(count);
});
