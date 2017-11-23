import pygame
import pygame.camera
from pygame.locals import *

IMG_PATH = "img/cat.jpg"

def set_rows_to_color(pixel_array, start, end, color):
    for i in range(start, end):
        row = pixel_array[:, i]
        for j in range(0, len(row)):
            row[j] = color

def display_surface(surface):
    screen = pygame.display.set_mode((800, 600), 0)
    screen.blit(surface, (0,0))
    pygame.display.flip()

    going = True
    while going:
        events = pygame.event.get()
        for e in events:
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                going = False

def transform_by_kernel(pixel_array, kernel):
    radius = len(kernel) // 2
    width, height = pixel_array.shape
    for x in range(0, len(pixel_array)):
        column = pixel_array[x]
        for y in range(0, len(column)):
            #if x % 10 == 0 and y % 10 == 0:
            #    print("{},{}".format(x, y))
            pixel_array[x, y] = transform_pixel(pixel_array, x, y, kernel, radius, width, height)

def transform_pixel(pixel_array, x, y, kernel, radius, width, height):
    upper_sum = 0.0
    lower_sum = 0.0

    ctr = 0
    for i in range(x - radius, x + radius + 1):
        for j in range(y - radius, y + radius + 1):
            if i >= 0 and i < width and j >= 0 and j < height:
                ctr += 1
                lower_sum += kernel[i - x + radius][j - y + radius]
                upper_sum += pixel_array[i, j] * kernel[i - x + radius][j - y + radius]
    return int(upper_sum / lower_sum)
            


surface = pygame.image.load(IMG_PATH)

array = pygame.PixelArray(surface)


avg_kernel = [[1]]
transform_by_kernel(array, avg_kernel)
display_surface(array.make_surface())


    
