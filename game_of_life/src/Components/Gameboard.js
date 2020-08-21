import React from "react"
import {Link,Route} from "react-router-dom"
import Grid from "./Grid.js"


function Gameboard(){
    return(
        <div>
            <div className = 'main-space'>
                <h1>Game of life board</h1>
                <p>This will start as a 15 x 15, and then get more complex hopefully</p>
                <div className = 'grid' style = {Grid}>
                    


                </div>
                    
                

            
            
            </div>
            
        </div>
    )
}

export default Gameboard;