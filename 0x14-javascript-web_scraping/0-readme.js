#!/usr/bin/node

/* path to file parsed as CMD args */
const filePath = process.argv[2];

const fs = require('fs');

fs.readFile(filePath, (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
});
