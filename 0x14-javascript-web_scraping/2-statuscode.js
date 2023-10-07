#!/usr/bin/node

/* url to process */
const urlReq = process.argv[2];

const request = require('request');

request(urlReq, (error, response, body) => {
  if (error) throw error;
  console.log('code:', response.statusCode);
});
