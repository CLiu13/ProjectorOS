import pygame
from math import pi

pygame.init()

#Sets our color values
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

#Create our variables
b1 = input("Please enter the 1st base height: ")
b2 = input("Please enter the 2nd base height: ")
h = input("Please enter the height: ")

# Set the height and width of the screen
screen = pygame.display.set_mode((1680,1050))

pygame.display.set_caption("Trapezoid Function")

# Clear the screen and set the screen background
surface.fill(white)

#Translate input to coordinates
xp1 = 700-(int(b2))/2
yp1 = 700
xp2 = 700+(int(b2))/2
yp2 = 700
xp3 = 700-(int(b1))/2
yp3 = 700+int(h)
xp4 = 700+(int(b1))/2
yp4 = 700+int(h)

#Draw trapezoid
pygame.draw.line(screen, green, [xp1,yp1],[xp2,yp2], 5) #Display, color, 1st coord, 2nd coord, width
pygame.draw.line(screen, green, [xp2,yp2],[xp4,yp4], 5)
pygame.draw.line(screen, green, [xp4,yp4],[xp3,yp3], 5)
pygame.draw.line(screen, green, [xp3,yp3],[xp1,yp1], 5)

#Updates the screen
pygame.display.update()
