#!/usr/bin/node
var fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    console.log(err);
  }
});
