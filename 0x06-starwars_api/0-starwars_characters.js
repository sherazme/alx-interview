#!/usr/bin/node
const requests = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length > 2) {
  requests(`${API_URL}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const charactersURL = JSON.parse(body).characters;
    const charactersName = charactersURL.map(
      url => new Promise((resolve, reject) => {
        requests(url, (promiseErr, __, charactersReqBody) => {
          if (promiseErr) {
            reject(promiseErr);
          }
          resolve(JSON.parse(charactersReqBody).name);
        });
      }));

    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(allErr => console.log(allErr));
  });
}
