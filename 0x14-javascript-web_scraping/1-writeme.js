#!/usr/bin/node

/* path to file parsed as CMD args */
const filePath = process.argv[2];
const writeContent = process.argv[3];

const fs = require('fs');

fs.writeFile(filePath, writeContent, (err) => {
  if (err) throw err;
});
