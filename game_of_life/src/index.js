import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();


/** TODO LIST >>>>>>>>>>>
 * First thing > seperate pages > Build mobile first > if possible emphasize speed
 * Have a mina page with minimal controls A start random, the game itself and then a pop out with information
 * Information page will have an overview of the game of life > history of game of life> 
 * The side pop out will also have configuration options > random > random num cells populated , etc.
 * otherwise run will run > might have a color and black and white mode
 * Include gen counter.
 * 
 * 
 * Game page will need grid maker > color randomizer > black and white option > night mode
 * speed > 
 * 
 * Build grid > start with a predefined object of objects > object will have two dimensions x, y and an alive or dead tracker > color as well
 * while run != True things are still
 * ANY INPUT Should pause the game ? 
 * Have options to pause game, reset game, step forward one.
 * ADD SOUND????? different colors when exiting game will make x sound? Use all sounds from same key, key change after 100 generations only certain colors make sounds?
 * 
 */