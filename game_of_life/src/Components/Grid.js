import React from 'react'

function Grid(){
    return{
        display: 'grid',
        gridTemplateColumns: `repeat(${15}, 20px)`,
        gridTemplateRows: `repeat(${15}, 20px)`
    }
}

export default Grid
