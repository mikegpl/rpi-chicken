import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

class Capture(object):
    def __init__(self):
        self.size = (640,480)
        self.display = pygame.display.set_mode(self.size, 0)

        self.clist = pygame.camera.list_cameras()
        if not self.clist:
            raise ValueError("Sorry, no cameras detected.")
        self.cam = pygame.camera.Camera(self.clist[0], self.size)
        self.cam.start()
        
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def simple_capture(self):
        return self.cam.get_image(self.snapshot)

    def capture_with_thresholding(self):
        thresholded = pygame.surface.Surface(self.size, 0, self.display)
        self.snapshot = self.simple_capture()
        pygame.transform.threshold(thresholded, self.snapshot, (0, 128, 128), (90,170,170), (0,0,0), 2)
        return thresholded
        
    def get_and_update(self):
        try:
            if self.cam.query_image():
                self.snapshot = self.capture_with_thresholding()
        except Exception as e:
            print(e)

        self.display.blit(self.snapshot, (0,0))
        pygame.display.flip()

    def main(self):
        going = True
        while going:
            events = pygame.event.get()
            for e in events:
                if e.type == KEYDOWN and e.key == K_ESCAPE:
                    self.cam.stop()
                    going = False

            self.get_and_update()
