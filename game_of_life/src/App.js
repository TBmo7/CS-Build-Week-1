import React from 'react';
import logo from './logo.svg';
import './App.css';
import {Route} from "react-router-dom"
import Gameboard from "./Components/Gameboard"
function App() {
  return (
    <div className="App">
      This will be the game of life
    <Gameboard/>

    </div>
  );
}

export default App;
