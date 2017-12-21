import pyximport

pyximport.install()

from lab2 import pygame_utils as pgu
from lab3 import edge_utils as eu
from lab2 import blur_utils as bu
from main2 import transform_by_kernel
import numpy as np

IMG_PATH = "img/sobeltest.png"

# values determined experimentally
UPPER_THRESHOLD = 45 ** 3
LOWER_THRESHOLD = 40 ** 3


def masked_surface_array(surf, kernel):
    return transform_by_kernel(surf, kernel)


def sobel_operator(surface, sobel_sum):
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
    radius = 1

    for x in range(0, width):
        for y in range(0, height):
            by_gx[x][y] = bu.transform_pixel(old_array, x, y, radius, width, height, gx, sobel_sum)
            by_gy[x][y] = bu.transform_pixel(old_array, x, y, radius, width, height, gy, sobel_sum)

    del old_array
    return by_gx, by_gy


def canny_edge_detection(surf, sobel_sum=5.0):
    """
    Performs Canny edge detection on surface surf, change sobel_sum to adjust brightness
    """
    by_gx, by_gy = sobel_operator(surf, sobel_sum)
    width = surf.get_width()
    height = surf.get_height()

    def pixel_value(x_pos, y_pos):
        return np.sqrt(np.power(by_gx[x_pos][y_pos], 2) + np.power(by_gy[x_pos][y_pos], 2))

    for x in range(0, width):
        for y in range(0, height):
            value = pixel_value(x, y)
            pixel_product = np.product(value)
            if pixel_product > UPPER_THRESHOLD:
                surf.set_at((x, y), np.minimum(np.array([255, 255, 255]), value))
            elif pixel_product < LOWER_THRESHOLD:
                surf.set_at((x, y), (0, 0, 0))
            else:
                end_loop = False
                for xx in [-1, 0, 1]:
                    if end_loop:
                        break
                    for yy in [-1, 0, 1]:
                        if 0 <= x + xx < width and 0 <= y + yy < height:
                            adjacent_value = pixel_value(x + xx, y + yy)
                            if np.product(adjacent_value) > UPPER_THRESHOLD:
                                surf.set_at((x, y), np.minimum([255, 255, 255], adjacent_value))
                                end_loop = True
                                break
                else:
                    surf.set_at((x, y), (0, 0, 0))


if __name__ == "__main__":
    img_surface = pgu.img_to_surface(path=IMG_PATH)
    img_surface = eu.surf_to_greyscale(img_surface)
    img_surface = transform_by_kernel(img_surface, bu.gaussian_kernel(size=1))
    canny_edge_detection(img_surface, 3.5)
    pgu.display_surface(img_surface, img_surface.get_width(), img_surface.get_height())
