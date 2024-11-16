#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/';
const movieId = process.argv[2];
request(url + 'films/' + movieId, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  Promise.all(
    characters.map(
      (url) =>
        new Promise((resolve, reject) =>
          request(url, (error, response, body) =>
            error ? reject(error) : resolve(JSON.parse(body).name)
          )
        )
    )
  )
    .then((names) => names.forEach((name) => console.log(name)))
    .catch((error) => console.log(error));
});
