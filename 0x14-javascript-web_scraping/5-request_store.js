#!/usr/bin/node

/* path to file parsed as CMD args */
const filePath = process.argv[3];
const urlReq = process.argv[2];

const fs = require('fs');
const request = require('request');

request(urlReq, (error, response, body) => {
  if (error) throw error;
  fs.writeFile(filePath, body, (err) => {
    if (err) throw err;
  });
});
