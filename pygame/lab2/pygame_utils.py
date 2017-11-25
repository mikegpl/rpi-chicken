import pygame
from pygame.locals import *

def img_to_surface(path):
    return pygame.image.load(path)

def surface_to_array(surface):
    return pygame.PixelArray(surface)

def surface_to_img(surface, path):
    pygame.image.save(surface, path)

def display_surface(surface, width = 200, height = 200):
    screen = pygame.display.set_mode((width, height), 0)
    screen.blit(surface, (0,0))
    pygame.display.flip()

    going = True
    while going:
        events = pygame.event.get()
        for e in events:
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                going = False
                
