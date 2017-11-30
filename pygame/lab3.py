import pyximport
import pygame
from lab2 import pygame_utils as pgu

pyximport.install()
from lab2 import blur_utlis as bu

def get_array_for_masks(width, height, mask_count):
    return np.zeros((width, height, mask_count))

def transform_by_mask(surface, target, mask_index, mask):
    array = pygame.PixelArray(surface)
    width, height = array.shape
    for x in range(0, width):
        for y in range(0, height):
            target[x, y, mask_index] = bu.rgb2int(*bu.mask_pixel(array, x, y, mask))
            
    del array
     
    
