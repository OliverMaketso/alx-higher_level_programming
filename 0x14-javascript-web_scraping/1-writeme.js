#!/usr/bin/node
const fs = require('fs');
const path = process.argv[2];
const data = process.argv[3];
fs.writeFile(path, data, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});