import pygame
import pygame_gui
import random

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

# GUI CREATION BELOW

number_of_cells = 25

grid = {}
for x in range(number_of_cells):
    for y in range(number_of_cells):
        grid[(x,y)] = {'Alive':False, 'Age':0, 'Neighbors':0}

def randomize(grid_in):
    alive_out = {}
    for i in grid_in:
        x,y = i
        choice = random.randint(0,1)
        if choice == 1:
            alive_out[(x,y)] = {'Alive':True}
    return alive_out

def simulate(grid_in,dict_in,value):
    current_grid = grid_in
    current_dict = dict_in 
    i = 0
    while i is not value:
        inner_grid = current_grid
        inner_dict = rules_of_life(inner_grid,current_dict)
        i += 1
        current_dict = inner_dict
    return current_dict

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
    
        
    alive = {}
    generation = 0
    

    grid_in2 = grid_in

    for i in grid_in2:
        x,y = i
        if (x,y) in alive_in:
            alive[(x,y)] = {'Alive':True}
    
    
    for i in grid_in2:
        
        alive_neighbors = 0
        dead_neighbors = 0
        
        x,y = i
        
        
        #TOP ROW OF NEIGHBORS
        
        if (x-1) > -1 and (y-1) > -1: #check "upper left neighbor"
            
            if(x-1,y-1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if  (y-1) > -1: #check neighbor directly above
                        
            if (x,y-1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1
        
        if (x+1) < (number_of_cells) and  (y-1) > -1: #check neighbor "upper right"
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
        
        if  (x+1) < (number_of_cells): #check neighbor to the right
            if (x+1,y) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        ##BOTTOM ROW OF NEIGHBORS##

        if (x-1) > -1 and  (y+1) < (number_of_cells): #check neighbor below to the left
            if (x-1,y+1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if (y+1) < (number_of_cells): #check neighbor directly below
            if (x,y+1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

        if (x+1) < (number_of_cells) and  (y+1) < (number_of_cells): #check neighbor below right
            if (x+1,y+1) in alive_in:
                alive_neighbors += 1
            else:
                dead_neighbors += 1

         
        
        alive_dict = alive
        dead_dict = alive

        
        if (x,y) in alive_in:
            
            if alive_neighbors < 2 or alive_neighbors > 3:
                
                dead_dict = dead(alive,x,y)
                              
        elif alive_neighbors == 3:
            
            alive_dict = grow(alive,x,y)
    
    alive.update(mergedict(alive_dict,dead_dict))
        
    #generation +=1    
        
    return alive
        
def main():
    

    
    pygame.init()
    generation = 0
    alive_outer = {}
    clock = pygame.time.Clock()
    #formula for screen size should be (cell width * cell number) + (margin * cell number) + margin width
    cell_display = (width * number_of_cells) + ( margin * number_of_cells) + margin
    screen = pygame.display.set_mode((cell_display + 100,cell_display ))
    done = False
    running = False
    pygame.display.set_caption("The Game of Life")
    manager = pygame_gui.UIManager((cell_display + 100, cell_display + 150))
    options_panel = pygame_gui.elements.UIPanel(starting_layer_height = 0, relative_rect = pygame.Rect(((627,3),(103,625))), manager = manager)
    run_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((630,5), (97,50)),text = 'Start/Stop', manager = manager)
    rand_button = pygame_gui.elements.UIButton(relative_rect = pygame.Rect((630,60), (97,50)),text = 'Random', manager = manager)

    set_speed = 333
    #pygame_gui.elements.ui_panel
    #CLICK TO SET INITIAL STATE
    while not done:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                done = True
            
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                if (row,column) in grid:
                    if grid[(row,column)]['Alive'] == False:
                        grid[(row,column)].update({'Alive': True})
                        alive_outer[(row,column)] = {'Alive': True}
                    else:
                        grid[(row,column)].update({'Alive':False})
                        if (row,column) in alive_outer:
                            alive_outer.pop((row,column))
            
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == run_button:
                        if running == False:
                            print('running')
                            running = True
                        else:
                            print('not running')
                            running = False
                    if event.ui_element == rand_button:
                    
                        alive_outer = randomize(grid)
                    
            #get rid of this below
            # TO IMPLEMENT : RANDOM BUTTON
            # STEP AHEAD BUTTON
            # SPEED                                 
            #elif event.type == pygame.USEREVENT:
                #if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    #if event.ui_element == rand_button:
                    
                        #alive_outer = randomize(grid)
                    #if running == False:
                        #print('running')
                        #running = True
                    #else:
                        #print('not running') 
                        #running = False
            manager.process_events(event)            
        manager.update(time_delta)
        if running == True:
            
            this_this = rules_of_life(grid,alive_outer)
            
            alive_outer = this_this
            generation += 1
            pygame.time.wait(set_speed)
        #Checks for alive tiles and changes color accordingly
        for row in range(number_of_cells):
            for column in range (number_of_cells):
                color = WHITE
                if (row,column) in alive_outer:
                    color = GREEN
                pygame.draw.rect(screen,
                                color,
                                [(margin + width) * column + margin,
                                (margin + height) * row + margin,
                                width,
                                height])
                
        clock.tick(60) #limit to 60 FPS
        manager.draw_ui(screen)
        pygame.display.flip()
    


            

if __name__ == "__main__":
    main()

    class Layout():
        def is_alive(self, x, y):
            return self.get_bool(x,y,'alive')
        
        def render(self):
            alive = self.is_alive