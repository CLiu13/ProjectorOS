import pygame
from pygame.locals import*
from transfunction import transfunction
from screenres import screenres
from PIL import Image
import ImageDraw
import time
import sys

x = screenres.width/2
y = screenres.height/2
t = time.strftime('%l:%M%p %Z')
blankimg = Image.open(sys.argv[1])
draw = ImageDraw.Draw(blankimg)
draw.text((x,y), t, (255, 255, 255))
blankimg.save(sys.argv[2])

w = screenres.width
h = screenres.height

oldimg=Image.open(sys.argv[2])
newimg=oldimg.resize((w,h), Image.ANTIALIAS)
newimg.save("/home/pi/ProjectorOS/tools/images/resize.jpg")

img=Image.open("/home/pi/ProjectorOS/tools/images/resize.jpg")
xc=float(sys.argv[3])
yc=float(sys.argv[4])
transimg=transfunction.project(img, xc, yc)
transimg.save("/home/pi/ProjectorOS/tools/images/new.jpg")
time.sleep(5)

loadimg=pygame.image.load("/home/pi/ProjectorOS/tools/images/new.jpg")

pygame.init()

white = (255, 255, 255)
screen = pygame.display.set_mode((w,h))
screen.fill((white))

screen.blit(loadimg,(0,0))
pygame.display.update()
time.sleep(15)

