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
size = [1000, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Trapezoid Function")

#Loops until the use clicks the close button
done = False
clock = pygame.time.Clock()

# Clear the screen and set the screen background
screen.fill(white)

"""pygame.draw.line(screen, green, [200,200],[500,200], 5)
pygame.draw.line(screen, green, [200,200],[300,300], 5)
pygame.draw.line(screen, green, [300,300],[400,300], 5)
pygame.draw.line(screen, green, [400,300],[500,200], 5)"""
#Just keeping the above lines if we still need it

pygame.draw.rect(screen, black, [400, 200, 200, 200])

#pygame.draw.rect(screen, black, [how far across from the left, how far from
#the top, how wide, how long])

pygame.draw.polygon(screen, black, [[400,200], [200,200], [400,400]])
pygame.draw.polygon(screen, black, [[600,200], [800,200], [600,400]])

#Updates the screen
pygame.display.update()

pygame.quit()
quit()
