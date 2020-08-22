import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
#Defining Colors
height = 20
width = 20
margin = 5
#Make a 2d grid with age and Neighbor tracking
#hopefully later on to make finding cells to kill, stay or grow
#create a search function with a hash table(s)? so if Alive, and neghbors >= 2
# it gets dropped in the keep alive
#less than that, the cell dies and the age is reset
#more than that it runs a spawn function
#change colors based on generation !
grid = {}
for x in range(15):
    for y in range(15):
        grid[(x,y)] = {'Alive':False, 'Age':0, 'Neighbors':0}

#hash table to hold cells that are alive to prevent excessive executions
#alive = {} #alive[x] = True

def i_am_alive(grid_in):
    #THIS IS A BONUS THING TO ADD AFTER EVERYTHING WORKS
    #checks to see if the cell is alive and populates the hash table
    for x in grid_in:
        if grid_in[x]['Alive'] == True:
            alive[x] = True
        elif grid_in[x] in alive:
            del alive[x]
    
    """
    if grid[cell_in]['Alive'] == True:
        alive[cell_in] = True
    else
        del alive[cell_in]    
    """
def get_neighbors(cell_in):
    #will need to splt the tuple somewhere either here, or in rules of life
    print(cell_in)
    

def rules_of_life(grid_in):
    #searches grid for alive tiles
    #can also put alive cells in hash table for quicker access
    #Test 1 below > Works > returns something > further testing required
    #!!!!!!!!!!!!# THIS SHOULD JUST TAKE IN THE CELL > UPDATE IT AND THEN RETURN IT BACK INTO THE MAIN ARRAY!!!!!#

        
    #alive = {}
    
    



    # below, just x is the coordinates
    #grid_in[x] is the object assigned to that
    #checking the neighbors below might be able to be it's own function just for cleaner code

    for i in grid_in:
        alive_neighbors = 0
        dead_neighbors = 0
        # set a list of variables here to all possibilites
        # create a function that takes two inputs and increments counters as needed instead or retyping retyping
        x,y = i
        ax = x - 1 # this is the coord of current cell's x coord - 1
        ay = y - 1 # this is the coord of current cell's y coord - 1
        bx = x + 1 # this is the coord of current cell's x coord + 1 
        by = y + 1 # this is the coord of current cell's y coord + 1
        #TOP ROW OF NEIGHBORS
        if (x-1) > -1 and (y-1) > -1: #check "upper left neighbor"
            if grid_in[(x-1,y-1)]['Alive'] == True:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if (y-1) > -1: #check neighbor directly above
            if grid_in[(x+0,y-1)]['Alive'] == True:
                alive_neighbors += 1
            else:
                dead_neighbors += 1
        
        if (x+1) < 14 and  (y-1) > -1: #check neighbor "upper right"
            if grid_in[(x+1,y-1)]['Alive'] == True:
                alive_neighbors += 1
            else:
                dead_neighbors += 1
        ##MIDDLE ROW OF NEIGHBORS##

        if (x-1) > -1: #check neighbor to the left
            if grid_in[(x-1,y+0)]['Alive'] == True:
                alive_neighbors += 1
            else:
                dead_neighbors += 1
        
        if (y+1) < 14: #check neighbor to the right
            if grid_in[(x+0,y+1)]['Alive'] == True:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        ##BOTTOM ROW OF NEIGHBORS##

        if (x-1) > -1 and  (y+1) < 14: #check neighbor below to the left
            if grid_in[(x-1,y+1)]['Alive'] == True:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if (y+1) < 14: #check neighbor directly below
            if grid_in[(x+0,y+1)]['Alive'] == True:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if (x+1) < 14 and  (y+1) < 14: #check neighbor below right
            if grid_in[(x+1,y+1)]['Alive'] == True:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        #final place for logic here
        #if a live cell has  < 2 alive neighbors or > than 3 neighbors it dies
        # else it lives
        # if a dead cell has 3 alive neighbors it becomes alive
        # 
        if grid_in[x,y]['Alive'] == True:
            if alive_neighbors < 2 or alive_neighbors > 3:
                grid_in[x,y]['Alive'] = False
        if grid_in[x,y]['Alive'] == False:
            if alive_neighbors == 3:
                grid_in[x,y] = True       
        #checking something here will not remain in final
        #print(grid_in)
def main():
    

    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((380,380))
    done = False
    running = False
    pygame.display.set_caption("The Game of Life")

    #CLICK TO SET INITIAL STATE
    while not done:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                done = True
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                if grid[(row,column)]['Alive'] == False:
                    grid[(row,column)]['Alive'] = True
                else:
                    grid[(row,column)]['Alive'] = False
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_SPACE:
                    
                    if running == False:
                        print('running')
                        running = True
                    else:
                        print('not running') 
                        running = False
        #print(grid)
        #TEST ONGOING
        if running == True:
            (rules_of_life(grid))
            #i_am_alive(grid)
            #print(alive)
            
        #Checks for alive tiles and changes color accordingly
        for row in range(15):
            for column in range (15):
                color = WHITE
                if grid[(row,column)]['Alive'] is True:
                    color = GREEN
                pygame.draw.rect(screen,
                                color,
                                [(margin + width) * column + margin,
                                (margin + height) * row + margin,
                                width,
                                height])
        
        
        
        #|Animation test function Below, should be removed **Epilepsy Warning**
        #if running == True:
                #else:
            #for x in grid:
                #if grid[x]['Alive'] == False:
                    #grid[x]['Alive'] = True
                #else:
                    #grid[x]['Alive'] = False


        #TESTING LOOP FLIPS COLOR
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #done = True
            #else:
                #for x in grid:
                    #if grid[x]['Alive'] == False:
                        #grid[x]['Alive'] = True
                    #else:
                        #grid[x]['Alive'] = False
        #This changes color based on what's going on
        
    #pygame.draw.rect(screen,WHITE,[0,0,height,width]) #draws a rect at the upper left hand side of the screen
        
        clock.tick(60) #limit to 60 FPS
        
        pygame.display.flip()
    


            

if __name__ == "__main__":
    main()

    class Layout():
        def is_alive(self, x, y):
            return self.get_bool(x,y,'alive')
        
        def render(self):
            alive = self.is_alive