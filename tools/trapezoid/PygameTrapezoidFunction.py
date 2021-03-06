import pygame
import time
from math import pi
from screenres import screenres

pygame.init()

#Sets our color values
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)

#Create our dimensions
width = screenres.width
height = screenres.height

#Create our sizes
b1 = int(width*2/3)
b2 = int(width/3)
h = int(height/3)

#Create our center
centx = int(width/2)
centy = int(height/2)

# Set the height and width of the screen
screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Trapezoid Function")

# Clear the screen and set the screen background
screen.fill(black)

#Create our coordinates
xp1 = int(centx - b1/2) 
yp1 = int(centy + h/2)
xp2 = int(centx + b1/2)
yp2 = int(centy + h/2)
xp3 = int(centx - b2/2)
yp3 = int(centy - h/2)
xp4 = int(centx + b2/2)
yp4 = int(centy - h/2)

#Draw trapezoid filled in
pygame.draw.polygon(screen, green, [(xp1,yp1),(xp2,yp2),(xp4,yp4),(xp3,yp3)], 0)

#Updates the screen
pygame.display.update()

#Freeze the screen for 10 seconds
time.sleep(10)
