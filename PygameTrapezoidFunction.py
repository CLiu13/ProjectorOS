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
size = [1000, 1000]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Trapezoid Function")

# Clear the screen and set the screen background
surface.fill(white)

pygame.draw.line(screen, green, [200,200],[500,200], 5)
pygame.draw.line(screen, green, [200,200],[300,300], 5)
pygame.draw.line(screen, green, [300,300],[400,300], 5)
pygame.draw.line(screen, green, [400,300],[500,200], 5)

#Updates the screen
pygame.display.update()
