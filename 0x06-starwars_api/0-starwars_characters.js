#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/';
const movieId = process.argv[2];
request(url + 'films/' + movieId, (error, _, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (error, _, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
