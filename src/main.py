import sys
import time
import pygame
from pygame.locals import*
from PIL import Image
from transfunction import transfunction
from screenres import screenres

w = screenres.width
h = screenres.height

oldimg=Image.open(sys.argv[1])
newimg=oldimg.resize((w,h), Image.ANTIALIAS)
newimg.save("/home/pi/ProjectorOS/tools/images/resize.jpg")

img=Image.open("/home/pi/ProjectorOS/tools/images/resize.jpg")
xc=float(sys.argv[2])
yc=float(sys.argv[3])
coeffs=transfunction.coeffs(w, h, xc, yc)
transimg=transfunction.project(img, coeffs)
transimg.save("/home/pi/ProjectorOS/tools/images/new.jpg")
time.sleep(5)

loadimg=pygame.image.load("/home/pi/ProjectorOS/tools/images/new.jpg")

pygame.init()
screen = pygame.display.set_mode((w,h))

screen.blit(loadimg,(0,0))
pygame.display.update()
time.sleep(15)
