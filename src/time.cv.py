import cv2
import numpy
import pygame
from pygame.locals import*
from transfunction import transfunction
from screenres import screenres
from PIL import Image
import ImageDraw
import ImageFont
import time
import sys

blankimg = Image.open(sys.argv[1])

font_path = "/home/pi/ProjectorOS/tools/fonts/FreeMono.ttf"
font = ImageFont.truetype(font_path, 250, encoding="unic")

w = screenres.width
h = screenres.height

pygame.init()
screen = pygame.display.set_mode((w,h))

xc=float(sys.argv[2])
yc=float(sys.argv[3])

x = 0
y = screenres.height/2
 
def showtime():
  timeimg = blankimg.copy()  	  
  draw = ImageDraw.Draw(timeimg)

  t = time.strftime('%l:%M:%S%p')
  draw.text((x,y), t, (255, 255, 255), font=font)

  cvimage = cv2.cvtColor(numpy.array(timeimg), cv2.COLOR_RGB2BGR)
  
  loadimg=transfunction.cv(cvimage, w, h, xc, yc)

  screen.blit(loadimg,(0,0))
  pygame.display.update()

lastime = time.time()

while True:
  showtime()
  delta = int(round((time.time() - lastime) * 1000))
  print(delta)
  lastime = time.time()
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        sys.exit()
    
 
