#!/usr/bin/node

const request = require('request');

const movie = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movie}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
