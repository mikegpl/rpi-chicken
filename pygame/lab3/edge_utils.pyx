import numpy as np
import pygame

# todo this can be casual .py file

# edge detection
def gx():
    return np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

def gy():
    return np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# using surface.pixels3d
def to_greyscale(pixel_array_3d):
    return pixel_array_3d.dot([0.298, 0.587, 0.114])[:, :, None].repeat(3, axis=2)

def surf_to_greyscale(surface):
    return pygame.surfarray.make_surface(to_greyscale(pygame.surfarray.pixels3d(surface)))
