#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const characterId = '18';
  let count = 0;

  films.forEach((film) => {
    if (film.characters.some((url) => url.includes(characterId))) {
      count++;
    }
  });

  console.log(count);
});
