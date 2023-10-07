#!/usr/bin/node

const charId = 'https://swapi-api.alx-tools.com/api/people/18/';

/* url to API */
const urlReq = process.argv[2];

const request = require('request');

request(urlReq, (error, response, body) => {
  if (error) throw error;
  response = JSON.parse(body);
  const movies = response.results;
  let i = 0;
  let count = 0;

  while (movies[i]) {
    try {
      if (movies[i].characters) {
        movies[i].characters.forEach((value, ind) => {
          if (value === charId) {
            count++;
          }
        });
      }
    } catch (error) {
      console.log(error);
    }
    i++;
  }

  console.log(count);
});
