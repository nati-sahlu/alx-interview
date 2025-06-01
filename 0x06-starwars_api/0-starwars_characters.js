#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const characters = JSON.parse(body).characters;

  const printCharacter = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (err, res, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(body).name);
      printCharacter(index + 1);
    });
  };

  printCharacter(0);
});

