#!/usr/bin/node
const request = require('request');

let url = process.argv[2];
console.log(url)

request(url, function (error, response) {
    console.log(`code: ${response.statusCode}`);
});