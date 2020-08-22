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


def main():
    

    pygame.init()
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((380,380))
    done = False
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
        #TESTING LOOP FLIPS COLOR
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            else:
                for x in grid:
                    if grid[x]['Alive'] == False:
                        grid[x]['Alive'] = True
                    else:
                        grid[x]['Alive'] = False
    
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
    #pygame.draw.rect(screen,WHITE,[0,0,height,width]) #draws a rect at the upper left hand side of the screen
        
        clock.tick(120) #limit to 60 FPS
        
        pygame.display.flip()
    


            

if __name__ == "__main__":
    main()

    class Layout():
        def is_alive(self, x, y):
            return self.get_bool(x,y,'alive')
        
        def render(self):
            alive = self.is_alive