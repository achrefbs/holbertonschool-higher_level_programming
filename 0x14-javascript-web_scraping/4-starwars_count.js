#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, res, body) {
  let c = 0;
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  for (let i = 0; json.results[i] !== undefined; i++) {
    if (json.results[i].characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
      c++;
    }
  }
  console.log(c);
});
