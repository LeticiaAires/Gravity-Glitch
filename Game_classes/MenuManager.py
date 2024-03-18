import os
import pygame
import sys
import random
rnd = random.Random()


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
        
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("teste Gravity Glitch")
        self.background_image = pygame.image.load("Assets/background2.jpg").convert()
        self.background_rect = self.background_image.get_rect()

    # Music icon settings
        self.music_icon_font = pygame.font.Font(self.font_path, 20)
        self.music_icon_on = self.music_icon_font.render("🔊", True, self.class_WHITE)
        self.music_icon_off = self.music_icon_font.render("🔇", True, self.class_WHITE)
        self.music_icon_rect = self.music_icon_on.get_rect(topright=(self.SCREEN_WIDTH - 10, 10))
        self.is_music_on = True  # Initial state

    def toggle_music(self):
        self.is_music_on = not self.is_music_on
        if self.is_music_on:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

    def draw_music_icon(self):
        if self.is_music_on:
            self.screen.blit(self.music_icon_on, self.music_icon_rect)
        else:
            self.screen.blit(self.music_icon_off, self.music_icon_rect)

    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = self.BUTTON_WIDTH + 20
            button_rect.h = self.BUTTON_HEIGHT + 10
        else:
            button_rect.w = self.BUTTON_WIDTH
            button_rect.h = self.BUTTON_HEIGHT

    def quitting(self):
        return "quit"


    def quitting():
        return "quit"