import pyximport

pyximport.install()

from lab2 import pygame_utils as pgu
from lab2 import blur_utils as bu
import pygame

IMG_PATH = "img/cat.jpg"
RES_PATH = "res.jpg"


def transform_by_kernel(surf, kernel):
    """
    :param surf: surface to be transformed
    :param kernel: kernel to be used for convolution
    :return: new surface
    """

    old_array = pygame.surfarray.pixels3d(surf)
    new_array = pygame.surfarray.array3d(surf)

    kernel_array, kernel_sum = kernel
    radius = len(kernel_array) // 2
    width, height, _ = old_array.shape

    for x in range(0, width):
        for y in range(0, height):
            new_array[x, y] = bu.transform_pixel(old_array, x, y, radius, width, height, kernel_array, kernel_sum)

    del old_array
    return pygame.surfarray.make_surface(new_array)


if __name__ == "__main__":
    surface = pgu.img_to_surface(path=IMG_PATH)
    kernel = bu.avg_kernel(size=3)
    pgu.display_surface(transform_by_kernel(surface, kernel))

    # surface = pygame.surfarray.make_surface(bu.to_grayscale(pygame.surfarray.pixels3d(surface)))
    # pgu.display_surface(transform_by_kernel(surface, bu.gy()))
