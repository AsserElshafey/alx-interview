const axios = require('axios');

async function getMovieCharacters(movieId) {
  try {
    const movieResponse = await axios.get(`https://swapi-api.alx-tools.com/api/films/${movieId}`);
    const characters = movieResponse.data.characters;

    for (const characterUrl of characters) {
      const characterResponse = await axios.get(characterUrl);
      console.log(characterResponse.data.name);
    }
  } catch (error) {
    console.error("Error retrieving movie data:", error);
  }
}

if (process.argv.length > 2) {
  const movieId = parseInt(process.argv[2]);
  getMovieCharacters(movieId);
} else {
  console.error("Please provide a movie ID as an argument.");
}
