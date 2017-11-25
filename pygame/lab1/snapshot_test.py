import pygame
import pygame.camera as pycam
from pygame.locals import *

PATH = "/dev/video0"
RES = (1024, 768)
FNAME = "xD.png"


pygame.init()
pycam.init()

cam = pycam.Camera(PATH, RES)
cam.start()
image = cam.get_image()
pygame.image.save(image, FNAME)
