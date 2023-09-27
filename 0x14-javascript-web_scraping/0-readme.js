#!/usr/bin/node

/* path to file parsed as CMD args */
const filePath = process.argv[2];

const fs = require('fs');

fs.readFile(filePath, (err, contents) => {
  if (err) throw err;
  console.log(contents.toString());
});
