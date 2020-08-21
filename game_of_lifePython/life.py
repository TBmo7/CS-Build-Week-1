import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
#Defining Colors

def main():
    

    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(60) #limit to 60 FPS

    height = 20
    width = 20
    margin = 5

    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    screen = pygame.display.set_mode((380,380))

    running = True
    for row in range(15):
        for column in range (15):
            color = WHITE
            pygame.draw.rect(screen,
                            color,
                            [(margin + width) * column + margin,
                            (margin + height) * row + margin,
                            width,
                            height])
    #pygame.draw.rect(screen,WHITE,[0,0,height,width]) #draws a rect at the upper left hand side of the screen
    pygame.display.flip()
    

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()

    class Layout():
        def is_alive(self, x, y):
            return self.get_bool(x,y,'alive')
        
        def render(self):
            alive = self.is_alive