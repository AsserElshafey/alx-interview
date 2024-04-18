#!/usr/bin/node
const request = require('request');

function getMovieCharacters(movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error("Error retrieving movie data:", error);
      return;
    }

    if (response.statusCode === 200) {
      const data = JSON.parse(body);
      const characters = data.characters;

      characters.forEach(characterUrl => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error("Error retrieving character data:", characterError);
            return;
          }

          if (characterResponse.statusCode === 200) {
            const characterData = JSON.parse(characterBody);
            console.log(characterData.name);
          } else {
            console.error(`Error getting character: ${characterUrl}`, characterResponse.statusCode);
          }
        });
      });
    } else {
      console.error(`Error retrieving movie data: ${response.statusCode}`);
    }
  });
}

if (process.argv.length > 2) {
  const movieId = parseInt(process.argv[2]);
  getMovieCharacters(movieId);
} else {
  console.error("Please provide a movie ID as an argument.");
}
