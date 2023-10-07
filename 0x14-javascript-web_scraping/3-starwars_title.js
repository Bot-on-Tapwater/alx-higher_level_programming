#!/usr/bin/node

const movieId = process.argv[2];

/* url to API */
const urlReq = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const request = require('request');

request(urlReq, (error, response, body) => {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
