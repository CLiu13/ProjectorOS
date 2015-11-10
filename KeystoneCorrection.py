raw=input("Please enter a percentage here (Omit %): ")
percent=int(raw)
if percent >= 100:
    print("\n")    
    print("Please enter a percentage less than 100%")
else:
    print("\n")
    print("You entered", percent, "%")
import pygame 
import sys
pygame.init()
screen = pygame.display.set_mode((1680,1050))
black = (0,0,0)
white = (255,255,255)
screen.fill(black)
pygame.display.set_caption('ProjectorOS')
pygame.draw.rect(screen, white, (500,500,500,500))
pygame.display.update()
_quit = False
    while not _quit:
        for e in pygame.event.get():
            if (e.type is KEYDOWN and e.key == K_RETURN
                    and (e.mod&(KMOD_LALT|KMOD_RALT)) != 0):
                pygame.display.toggle_fullscreen()
            if e.type is QUIT: _quit = True
            if e.type is KEYDOWN and e.key == K_ESCAPE: _quit = True
