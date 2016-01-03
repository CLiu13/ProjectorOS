import sys
import time
import pygame
from pygame.locals import*
from PIL import Image
from transfunction import transfunction
from screenres import screenres

w = screenres.width
h = screenres.height

oldimg=Image.open("/home/pi/ProjectorOS/tools/images/cute-cat.jpg")
newimg=oldimg.resize((w,h), Image.ANTIALIAS)
newimg.save("/home/pi/ProjectorOS/tools/images/resize-cat.jpg")

img=Image.open("/home/pi/ProjectorOS/tools/images/resize-cat.jpg")
xc=float(sys.argv[1])
yc=float(sys.argv[2])
transimg=transfunction.project(img, xc, yc)
transimg.save("/home/pi/ProjectorOS/tools/images/new-cat.jpg")
time.sleep(5)

loadimg=pygame.image.load("/home/pi/ProjectorOS/tools/images/new-cat.jpg")

pygame.init()

white = (255, 255, 255)
screen = pygame.display.set_mode((w,h))
screen.fill((white))

screen.blit(loadimg,(0,0))
pygame.display.update()
time.sleep(15)
