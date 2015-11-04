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
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
                break
        elif event.type == pygame.QUIT:
            done = True
            break
    if done:
      break

