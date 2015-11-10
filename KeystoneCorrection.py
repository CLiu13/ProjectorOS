import pygame 
import sys
pygame.init()
screen = pygame.display.set_mode((1680,1050))
black = (0,0,0)
white = (255,255,255)
screen.fill(black)
pygame.display.toggle_fullscreen()
pygame.draw.rect(screen, white, (500,500,500,500))
pygame.display.update()
