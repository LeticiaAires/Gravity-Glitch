import pygame
import math
from pygame.locals import *

FPS = 60

def frames_to_msec(frames, fps=FPS):
    return 1000.0 * frames / fps


class Bird(pygame.sprite.Sprite):

    WIDTH = HEIGHT = 32
    SINK_SPEED = 0.18
    CLIMB_SPEED = 0.3
    CLIMB_DURATION = 333.3

    def __init__(self, x, y, msec_to_climb, images):

        super(Bird, self).__init__()

        self.x, self.y = x, y
        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)

    def update(self, delta_frames=1):

        if self.msec_to_climb > 0:

            frac_climb_done = 1 - self.msec_to_climb/Bird.CLIMB_DURATION
            self.y -= (Bird.CLIMB_SPEED * frames_to_msec(delta_frames) *
                       (1 - math.cos(frac_climb_done * math.pi)))
            self.msec_to_climb -= frames_to_msec(delta_frames)

        else:

            self.y += Bird.SINK_SPEED * frames_to_msec(delta_frames)

    @property

    def image(self):
        return self._img_wingup if pygame.time.get_ticks() % 500 >= 250 else self._img_wingdown




    @property

    def mask(self):
        return self._mask_wingup if pygame.time.get_ticks() % 500 >= 250 else self._mask_wingdown




    @property

    def rect(self):
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)
