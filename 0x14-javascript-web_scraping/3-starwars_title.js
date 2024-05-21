#!/usr/bin/node
const request = require('request');

let id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
    console.log(error || JSON.parse(body).title);
});
