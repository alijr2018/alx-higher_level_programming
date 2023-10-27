#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Please provide the API URL as an argument.');
  process.exit(1);
}

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) => {
      return film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`) ? acc + 1 : acc;
    }, 0);

    console.log(count);
  }
});
