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

#Update 8/24/2020
#Need to change the way this prgram works due to an unexpected mutation
#Will have a function that runs over the array and populates a hashtable with only alive values
# Then have a function that searches over a copy of the array and then takes in a cell, checks alive neighbors and updates

grid = {}
for x in range(15):
    for y in range(15):
        grid[(x,y)] = {'Alive':False, 'Age':0, 'Neighbors':0}

#hash table to hold cells that are alive to prevent excessive executions
#alive_outer = {} #alive[x] = True

def i_am_alive(grid_in):
    #THIS IS A BONUS THING TO ADD AFTER EVERYTHING WORKS
    #checks to see if the cell is alive and populates the hash table
    #for i in grid_in:
        #x,y = i
        #if grid_in[(x,y)]['Alive'] == True:
            #alive[(x,y)] = {'Alive':True}
            #print(alive)
    pass
def get_neighbors(cell_in):
    #will need to splt the tuple somewhere either here, or in rules of life
    pass

def grow(dictin,x,y):
    #takes in a dict and determines if values are alive
    thisisadict = dictin
    thisisadict[(x,y)] = {'Alive':True}
    return thisisadict
def dead(dictin,x,y):
    #takes in a dict and makes things dead
    thisisadict = dictin
    thisisadict.pop((x,y))
    return thisisadict
def mergedict(alive,dead):
    #merges the two dicts into a single
    outdict = {}
    outdict.update(alive)
    outdict.update(dead)
    return outdict    
    
def rules_of_life(grid_in,alive_in):
    #searches grid for alive tiles
    #can also put alive cells in hash table for quicker access
    #Test 1 below > Works > returns something > further testing required
    #!!!!!!!!!!!!# THIS SHOULD JUST TAKE IN THE CELL > UPDATE IT AND THEN RETURN IT BACK INTO THE MAIN ARRAY!!!!!#
        
    alive = {}
    generation = 0
    

    grid_in2 = grid_in

    for i in grid_in2:
        x,y = i
        if (x,y) in alive_in:
            alive[(x,y)] = {'Alive':True}
    #print(alive)

    # below, just x is the coordinates
    #grid_in[x] is the object assigned to that
    #checking the neighbors below might be able to be it's own function just for cleaner code

    for i in grid_in2:





        print('alive in for loop')
        print(alive)
        alive_neighbors = 0
        dead_neighbors = 0
        # set a list of variables here to all possibilites
        # create a function that takes two inputs and increments counters as needed instead or retyping retyping
        x,y = i
        print(f'This is x {x} this is y{y}')
        ax = x - 1 # this is the coord of current cell's x coord - 1
        ay = y - 1 # this is the coord of current cell's y coord - 1
        bx = x + 1 # this is the coord of current cell's x coord + 1 
        by = y + 1 # this is the coord of current cell's y coord + 1
        
        #TOP ROW OF NEIGHBORS
        #print(grid_in[(x,y)].get('Alive'))
        if (x-1) > -1 and (y-1) > -1: #check "upper left neighbor"
            
            if(x-1,y-1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if  (y-1) > -1: #check neighbor directly above
            #print(grid_in[(x,y-1)]['Alive'])
            #print(grid_in[(x,y-1)])
            #for some reason this mutates into a bool when checked. changing tack            
            #test_check = grid_in2[(x,y-1)]
            #ham = type(test_check)
            #print(f'this is grid_in {x},{y}')
            #print(test_check)
            #print(type(test_check))
            
            if (x,y-1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1
        
        if (x+1) < 14 and  (y-1) > -1: #check neighbor "upper right"
            if (x+1,y-1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1
        ##MIDDLE ROW OF NEIGHBORS##

        if (x-1) > -1 : #check neighbor to the left
            if (x-1,y+0) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1
        
        if  (x+1) < 14: #check neighbor to the right
            if (x+1,y) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        ##BOTTOM ROW OF NEIGHBORS##

        if (x-1) > -1 and  (y+1) < 14: #check neighbor below to the left
            if (x-1,y+1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if (y+1) < 14: #check neighbor directly below
            if (x,y+1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if (x+1) < 14 and  (y+1) < 14: #check neighbor below right
            if (x+1,y+1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        #final place for logic here
        #if a live cell has  < 2 alive neighbors or > than 3 neighbors it dies
        # else it lives
        # if a dead cell has 3 alive neighbors it becomes alive
        # 
        
        alive_dict = alive
        dead_dict = alive

        
        if (x,y) in alive_in:
            
            if alive_neighbors < 2 or alive_neighbors > 3:
                print(f'REMOVING {x},{y}')
                print(f'ALIVE NEIGHBORS == {alive_neighbors}')
                #alive.pop(x,y)
                dead_dict = dead(alive,x,y)
            
            #elif alive_neighbors == 2 or alive_neighbors == 3:
                #alive[(x,y)] = {'Alive':True}
                #this might be wrong, can make three
                #grow(alive,x,y)
                #pass
            
        
                #grid_in2[x,y]['Alive'] = False       
        elif alive_neighbors == 3:
            
            print(f'ADDING {x},{y}')
            print(f'ALIVE NEIGHBORS == {alive_neighbors}')
            #grid_in2[x,y] = True
            #alive[(x,y)] = {'Alive':True}
            alive_dict = grow(alive,x,y)
    alive.update(mergedict(alive_dict,dead_dict))
        #This above probably has to move outside the loop to right before we return alive.
        #checking something here will not remain in final
        #print(grid_in)
        #alive = {}
    generation +=1    
    print(f'This is the {generation} {alive} ')    
    return alive
        
def main():
    #with open('debugfile.txt') as f:
        #read_data = f.read()

    
    pygame.init()
    alive_outer = {}
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
                    grid[(row,column)].update({'Alive': True})
                    alive_outer[(row,column)] = {'Alive': True}
                else:
                    grid[(row,column)].update({'Alive':False})
                    if (row,column) in alive_outer:
                        alive_outer.pop((row,column)) 
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
            this_this = rules_of_life(grid,alive_outer)
            #Check to see if a snapshot is update, or there is an update trickle
            #Might need to somehow wait here for the entire database to be updated, and then pass the update.
            alive_outer = this_this
            #i_am_alive(grid)
            #print(alive)
        
        #Checks for alive tiles and changes color accordingly
        for row in range(15):
            for column in range (15):
                color = WHITE
                if (row,column) in alive_outer:
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