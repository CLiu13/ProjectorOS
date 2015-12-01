import pygame
from math import pi

pygame.init()

#Sets our color values
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Trapezoid Function")

#Loops until the use clicks the close button
done = False
clock = pygame.time.Clock()

while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
            
# Clear the screen and set the screen background
surface.fill(white)

pygame.draw.line(screen, green, [0, 0], [50,30], 5)
pygame.display.flip()

"""pygame.draw.aalines(screen, green, (0,50),(50,0), True)
pygame.draw.aalines(screen, green, [75,-75],[-75,50], True)"""

#Updates the screen
pygame.display.flip()

pygame.quit()
quit()
