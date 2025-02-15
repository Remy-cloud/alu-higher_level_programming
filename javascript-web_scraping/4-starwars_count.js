#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  films.forEach(film => {
    if (film.characters.some(url => url.includes(`/people/${characterId}/`))) {
      count++;
    }
  });

  console.log(count);
});
