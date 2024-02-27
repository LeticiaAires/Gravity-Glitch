import pygame
import math
from pygame.locals import *

FPS = 60

def frames_to_msec(frames, fps=FPS):
    return 1000.0 * frames / fps

class Bird(pygame.sprite.Sprite):

    WIDTH = HEIGHT = 20
    SINK_SPEED = 0.1  # Reduced sink speed
    CLIMB_SPEED = 0.1  # Reduced climb speed
    CLIMB_DURATION = 150  # Reduced duration for a shorter and slower jump

    def __init__(self, x, y, msec_to_climb, images):
        super(Bird, self).__init__()

        self.x, self.y = x, y
        self.msec_to_climb = msec_to_climb
        self._img_wingup, self._img_wingdown = images
        self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)
        self.flap_frequency = 10  # Adjust this value for wing flap speed
        self.is_flapping = False

    def update(self, delta_frames=1):
        keys = pygame.key.get_pressed()

        if keys[K_SPACE]:
            self.flap()
        
        if self.msec_to_climb > 0:
            frac_climb_done = 1 - self.msec_to_climb / Bird.CLIMB_DURATION
            climb_factor = 1 - math.cos(frac_climb_done * math.pi)
            self.y -= Bird.CLIMB_SPEED * frames_to_msec(delta_frames) * climb_factor
            self.msec_to_climb -= frames_to_msec(delta_frames)
        else:
            self.y += Bird.SINK_SPEED * frames_to_msec(delta_frames)

        # Smoothly flap wings
        if self.is_flapping:
            self.flap_wings()

    def flap_wings(self):
        current_time = pygame.time.get_ticks()
        if current_time % 500 >= 250:
            self._img_wingup = pygame.transform.rotate(self._img_wingup, 20)
            self._mask_wingup = pygame.mask.from_surface(self._img_wingup)
        else:
            self._img_wingdown = pygame.transform.rotate(self._img_wingdown, -20)
            self._mask_wingdown = pygame.mask.from_surface(self._img_wingdown)
        self.is_flapping = False

    def flap(self):
        self.is_flapping = True

    @property
    def image(self):
        return self._img_wingup if pygame.time.get_ticks() % 500 >= 250 else self._img_wingdown

    @property
    def mask(self):
        return self._mask_wingup if pygame.time.get_ticks() % 500 >= 250 else self._mask_wingdown

    @property
    def rect(self):
        return Rect(self.x, self.y, Bird.WIDTH, Bird.HEIGHT)