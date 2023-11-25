import os
import pygame
import sys
import random
rnd = random.Random()

# Initialize pygame
pygame.init()
pygame.mixer.init()



# the class to manage the menu screens
class MenuManager:
    class_BLACK = (0, 0, 0)
    class_WHITE = (255,255,255)
    # Constants
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    BUTTON_WIDTH = 180
    BUTTON_HEIGHT = 60
    #font file and path
    font_filename = "your_font.ttf"
    font_path = os.path.join("Assets", font_filename)
    def __init__(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Menu Gravity Glitch")
        self.background_image = pygame.image.load("Assets/background2.jpg").convert()
        self.background_rect = self.background_image.get_rect()


    def run(self):
        pass

# Quit Pygame
pygame.mixer.quit()
pygame.quit()