#!/usr/bin/node

const request = require('request');

// Function to recursively request and print character names
const req = (arr, i) => {
  if (!arr || i === arr.length) return; // Ensure arr exists and has elements
  request(arr[i], (err, response, body) => {
    if (err) {
      console.error(`Error fetching character ${i + 1}:`, err);
    } else {
      try {
        const character = JSON.parse(body);
        console.log(character.name);
      } catch (parseError) {
        console.error(`Error parsing character ${i + 1} response:`, parseError);
      }
    }
    req(arr, i + 1); // Recursive call for next character
  });
};

// Request the film data
request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      console.error('Error fetching film data:', err);
    } else {
      try {
        const filmData = JSON.parse(body);
        const chars = filmData.characters;
        if (!chars || chars.length === 0) {
          console.error('No characters found for this film.');
        } else {
          req(chars, 0); // Start requesting characters
        }
      } catch (parseError) {
        console.error('Error parsing film data:', parseError);
      }
    }
  }
);
