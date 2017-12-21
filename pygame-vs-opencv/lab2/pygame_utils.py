import pygame
from pygame.locals import *


def img_to_surface(path):
    return pygame.image.load(path)


def surface_to_array(surface):
    return pygame.surfarray.pixels3d(surface)


def array_to_surface(array):
    return pygame.surfarray.make_surface(array)


def display_surface(surface, width=200, height=200):
    screen = pygame.display.set_mode((width, height), 0)
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    going = True
    while going:
        events = pygame.event.get()
        for e in events:
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                going = False
