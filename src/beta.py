import sys
import time
import pygame
from pygame.locals import*
from PIL import Image
from transfunction import transfunction
from screenres import screenres

w = screenres.width
h = screenres.height

img = Image.open(sys.argv[1])
xc = float(sys.argv[2])
yc = float(sys.argv[3])
transimg = transfunction.cv(img, w, h, xc, yc) 
transimg.save("/home/pi/ProjectorOS/tools/images/beta.jpg")
time.sleep(5)

loadimg = pygame.image.load("/home/pi/ProjectorOS/tools/images/beta.jpg")

pygame.init()
screen = pygame.display.set_mode((w,h))

screen.blit(loadimg,(0,0))
pygame.display.update()

while True:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_q:
        sys.exit()

