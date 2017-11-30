import pyximport
pyximport.install()

from lab2 import pygame_utils as pgu
from lab2 import blur_utils as bu
import pygame

IMG_PATH = "img/cat.jpg"
RES_PATH = "res.jpg"

def transform_by_kernel(old_surface, new_surface, kernel):
    old_array = pygame.PixelArray(old_surface)
    new_array = pygame.PixelArray(new_surface)

    kernel_array, kernel_sum = kernel
    radius = len(kernel) // 2
    width, height = old_array.shape

    for x in range(0, width):
        for y in range(0, height):
            new_array[x, y] = bu.rgb2int(
                *bu.transform_pixel(old_array, old_surface, x, y, radius, width, height, kernel_array, kernel_sum))

    del old_array
    del new_array
            
if __name__ == "__main__":
    source_surface = pgu.img_to_surface(path = IMG_PATH)
    target_surface = source_surface.copy()
    kernel = bu.avg_kernel(size = 3)
    
    transform_by_kernel(source_surface, target_surface, kernel)
    
    pgu.display_surface(target_surface)
    pgu.surface_to_img(target_surface, RES_PATH)
    
    
    


    
