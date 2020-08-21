import React from 'react'

const gridSize = 15;

const cellSize = gridSize => {
    if (gridSize === 15){
        return '20px'
    }
}

export const cellDisplay = (alive,gridSize) => {

    if (alive) {
        return{
            width: `${cellSize(gridSize)}`,
            height: `${cellSize(gridSize)}`,
            background: `white`
        }
    } else {
        return {
            width: `${cellSize(gridSize)}`,
            height: `${cellSize(gridSize)}`,
            background: 'black'
        }
    }



}

