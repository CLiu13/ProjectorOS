import cv2
import numpy
import pygame
from pygame.locals import*
from transfunction import transfunction
from screenres import screenres
import time
import sys

w = screenres.width
h = screenres.height

pygame.init()
screen = pygame.display.set_mode((w,h))

xc = float(sys.argv[1])
yc = float(sys.argv[2])

fontsize = float(sys.argv[3])

x = 0
y = h/4

blankimg = numpy.zeros((h, w, 3), numpy.uint8)
 
def showtime():

  text = time.strftime('%I:%M:%S%p')
  timeimg = cv2.putText(blankimg, text, (x,y), cv2.FONT_HERSHEY_DUPLEX, fontsize, tuple((0,255,0)), 7)
  
  loadimg=transfunction.cv(blankimg, w, h, xc, yc)

  screen.blit(loadimg,(0,0))
  pygame.display.update()

  blankimg[:] = tuple((0,0,0))

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
    
 
