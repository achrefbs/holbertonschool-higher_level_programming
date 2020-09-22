#!/usr/bin/node

const { get } = require('https');

const url = process.argv[2];

get(url, function (data) {
  console.log('code: ' + data.statusCode);
});
