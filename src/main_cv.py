import sys
import time
import pygame
from pygame.locals import*
import cv2
from transfunction import transfunction
from screenres import screenres

w = screenres.width
h = screenres.height

img = sys.argv[1]

xc = float(sys.argv[2])
yc = float(sys.argv[3])

opencvimg = cv2.imread(img)

b,g,r = cv2.split(opencvimg)
colorimg = cv2.merge([r,g,b])

resizeimg = cv2.resize(colorimg, (w,h))

loadimg = transfunction.cv(resizeimg, w, h, xc, yc) 

pygame.init()
screen = pygame.display.set_mode((w,h))

screen.blit(loadimg,(0,0))
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        sys.exit()

