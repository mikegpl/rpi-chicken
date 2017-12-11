import pyximport

pyximport.install()

from lab2 import pygame_utils as pgu
from lab3 import edge_utils as eu
from lab2 import blur_utils as bu
from main2 import transform_by_kernel
import numpy as np

IMG_PATH = "img/cat.jpg"


def masked_surface_array(surf, kernel):
    return transform_by_kernel(surf, kernel)


def sobel_operator(surface):
    """
    Returns two (width x height x 3) arrays containing RGB pixel values after convolution with Sobel masks.
    """
    old_array = pgu.surface_to_array(surface)
    width, height, _ = old_array.shape
    by_gx = np.zeros((width, height, 3))
    by_gy = np.zeros((width, height, 3))
    gx = eu.gx()
    gy = eu.gy()
    # some not so random constant for better visibility
    g_sum = 2
    radius = 1

    for x in range(0, width):
        for y in range(0, height):
            by_gx[x][y] = bu.transform_pixel(old_array, x, y, radius, width, height, gx, g_sum)
            by_gy[x][y] = bu.transform_pixel(old_array, x, y, radius, width, height, gy, g_sum)

    del old_array
    return by_gx, by_gy


def better_canny(surf):
    by_gx, by_gy = sobel_operator(surf)
    width = surf.get_width()
    height = surf.get_height()

    for x in range(0, width):
        for y in range(0, height):
            surf.set_at((x, y), np.sqrt(np.power(by_gx[x][y], 2) + np.power(by_gy[x][y], 2)))
            # todo - final canny stuff goes here


if __name__ == "__main__":
    surface1 = pgu.img_to_surface(path=IMG_PATH)
    surface1 = transform_by_kernel(surface1, bu.gaussian_kernel(size=6))
    surfa = eu.surf_to_greyscale(surface1)
    better_canny(surfa)
    pgu.display_surface(surfa, 200, 200)
