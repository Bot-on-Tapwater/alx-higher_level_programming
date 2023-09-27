#!/usr/bin/node

const movieId = process.argv[2];

/* url to API */
const urlReq = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

const request = require('request');

request(urlReq, (error, response, body) => {
  if (error) throw error;
  response = JSON.parse(body);
  const characters = response.characters;
  //   console.log(response);
  characters.forEach((value, ind) => {
    // console.log(value);
    request(value, (error, response, body) => {
      if (error) throw error;
      const char = JSON.parse(body);
      console.log(char.name);
    });
  });
});
