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
timeimg_path = sys.argv[1] + ".temp.jpg"
loadimg_path = sys.argv[1] + ".load.jpg"

font_path = "/home/pi/ProjectorOS/tools/fonts/FreeMono.ttf"
font = ImageFont.truetype(font_path, 300, encoding="unic")

w = screenres.width
h = screenres.height

pygame.init()
screen = pygame.display.set_mode((w,h))

xc=float(sys.argv[2])
yc=float(sys.argv[3])
coeffs = transfunction.coeffs(w, h, xc, yc)
print(coeffs)

x = 0
y = screenres.height/2

def showtime():
  timeimg = blankimg.copy()  	  
  draw = ImageDraw.Draw(timeimg)

  t = time.strftime('%l:%M:%S%p')
  draw.text((x,y), t, (255, 255, 255), font=font)

  timeimg=timeimg.resize((w,h), Image.ANTIALIAS)

  transimg=transfunction.project(timeimg, coeffs)
  transimg.save(loadimg_path)

  loadimg=pygame.image.load(loadimg_path)
  screen.blit(loadimg,(0,0))
  pygame.display.update()

for x in range(0,5):
  showtime()

