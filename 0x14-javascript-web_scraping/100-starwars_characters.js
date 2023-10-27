#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
  } else {
    const movie = JSON.parse(body);
    const characterUrls = movie.characters;

    function fetchCharacter (index) {
      if (index >= characterUrls.length) return;

      request(characterUrls[index], (charError, charResponse, charBody) => {
        if (!charError && charResponse.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        } else {
          console.error(`Failed to retrieve character: ${characterUrls[index]}`);
        }

        fetchCharacter(index + 1);
      });
    }

    fetchCharacter(0);
  }
});
