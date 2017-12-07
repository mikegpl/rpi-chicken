import pyximport

pyximport.install()

from lab2 import pygame_utils as pgu
from lab3 import edge_utils as eu
from lab2 import blur_utils as bu
from main2 import transform_by_kernel
import numpy as np
import pygame

IMG_PATH = "img/matterhorn.jpg"


def masked_surface_array(surface, kernel):
    return transform_by_kernel(surface, kernel)


def sobel_operator(surface):
    array_by_gx = pgu.surface_to_array(masked_surface_array(surface, eu.gx()))
    array_by_gy = pgu.surface_to_array(masked_surface_array(surface, eu.gy()))

    # pgu.display_surface(pgu.array_to_surface(array_by_gy), 450, 338)
    # pgu.display_surface(pgu.array_to_surface(array_by_gx), 450, 338)

    width, height, depth = array_by_gx.shape
    for x in range(0, width):
        for y in range(0, height):
            r1, g1, b1 = array_by_gx[x, y]
            r2, g2, b2 = array_by_gy[x, y]

            ra = min(255, np.sqrt(r1 ** 2 + r2 ** 2))
            ga = min(255, np.sqrt(g1 ** 2 + g2 ** 2))
            ba = min(255, np.sqrt(b1 ** 2 + b2 ** 2))

            if ra < 220 and ga < 220 and ba < 220:
                surface.set_at((x, y), (0, 0, 0))
            else:
                surface.set_at((x, y), (ra, ga, ba))

    '''
    To be done:
    
    Edge detection algorithm:
    X, Y = image.to_grayscale().sobel(g_x(), g_y())
    combine X and Y into one magnitude of gradient array G[x,y] = sqrt(X[x,y] ^ 2 + Y[x, y] ^2)
    define two thresholds - upper and lower and perform canny algorithm:
    if pixel value > upper -> set it to "hot" value
    else if pixel value > lower -> if it is adjacent to any "hot" pixel mark it as "hot"
    else -> discard pixel, set it to "cold" value
    
    '''


if __name__ == "__main__":
    surface = pgu.img_to_surface(path=IMG_PATH)
    surface = transform_by_kernel(surface, bu.gaussian_kernel(size=6))
    surface = eu.surf_to_greyscale(surface)
    sobel_operator(surface)
    pgu.display_surface(surface, width=450, height=338)
