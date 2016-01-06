import pygame
from pygame.locals import*
from transfunction import transfunction
from screenres import screenres
from PIL import Image
import ImageDraw
import ImageFont
import time
import sys

x = 0
y = screenres.height/2
font_path = "/home/pi/ProjectorOS/tools/fonts/FreeMono.ttf"
font = ImageFont.truetype(font_path, 300, encoding="unic")
w = screenres.width
h = screenres.height
black = (0,0,0)
pygame.init()
screen = pygame.display.set_mode((w,h))

def showtime():
  t = time.strftime('%l:%M:%S%p')
  blankimg = Image.open(sys.argv[1])
  draw = ImageDraw.Draw(blankimg)
  draw.text((x,y), t, (255, 255, 255), font=font)
  blankimg.save(sys.argv[2])
  oldimg=Image.open(sys.argv[2])
  newimg=oldimg.resize((w,h), Image.ANTIALIAS)
  newimg.save("/home/pi/ProjectorOS/tools/images/resize.jpg")

  img=Image.open("/home/pi/ProjectorOS/tools/images/resize.jpg")
  xc=float(sys.argv[3])
  yc=float(sys.argv[4])
  transimg=transfunction.project(img, xc, yc)
  transimg.save("/home/pi/ProjectorOS/tools/images/new.jpg")
  #time.sleep(5)

  loadimg=pygame.image.load("/home/pi/ProjectorOS/tools/images/new.jpg")
  screen.fill(black)
  screen.blit(loadimg,(0,0))
  pygame.display.update()
  time.sleep(1)

for x in range(0,5):
  showtime()

