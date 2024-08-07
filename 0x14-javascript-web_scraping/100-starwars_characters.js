#!/usr/bin/node
const request = require('request');
const api = 'https://swapi-api.hbtn.io/api/films/';
const movieId = process.argv[2];
const url = api + movieId;
request(url, function (error, respnse, body) {
  if (error) {
    console.log(error);
  }
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});