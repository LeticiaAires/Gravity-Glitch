import os
import pygame
import sys
import random
rnd = random.Random()

BLACK = (0, 0, 0)
# Initialize pygame
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 60

#font file and path
font_filename = "your_font.ttf"
font_path = os.path.join("Assets", font_filename)


# class for the settings menu
class SettingMenu(MenuManager):
    def __init__(self):
        super().__init__()
        self.title_setting_font = pygame.font.Font(font_path, 50)
        self.title_setting_text = self.title_setting_font.render("Settings", True, (255, 255, 255))
        self.title_setting_rect = self.title_setting_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

        self.return_font = pygame.font.Font(font_path, 30)
        self.return_button = self.return_font.render("Return", True, (0, 0, 0))
        self.return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 6, 500, BUTTON_WIDTH, BUTTON_HEIGHT)

        self.setting_font = pygame.font.Font(font_path, 40)
        self.musicon_text = self.setting_font.render("Music ON", True, (0, 0, 0))
        self.musicoff_text = self.setting_font.render("Music OFF", True, (0, 0, 0))

        self.musicon_rect = self.musicon_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.musicoff_rect = self.musicoff_text.get_rect(center=(SCREEN_WIDTH // 2, 300))

    def run(self):
        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.return_rect.collidepoint(mouse_pos):
                        print("The button 'Return' has been pressed")
                        running1 = False
                        return "main"
                    elif self.musicoff_rect.collidepoint(mouse_pos):
                        print("The button 'Music OFF' has been pressed")
                        pygame.mixer.music.stop()
                    elif self.musicon_rect.collidepoint(mouse_pos):
                        print("The button 'Music ON' has been pressed")
                        pygame.mixer.music.load('Assets/music_menu.wav')
                        pygame.mixer.music.play(-1)

                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
                self.update_button(self.musicon_rect, self.musicon_text, mouse_pos1)
                self.update_button(self.musicoff_rect, self.musicoff_text, mouse_pos1)
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_setting_text, (SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
            self.screen.blit(self.musicon_text, (self.musicon_rect.centerx - self.musicon_text.get_width() // 2, self.musicon_rect.centery - self.musicon_text.get_height() // 2))
            self.screen.blit(self.musicoff_text, (self.musicoff_rect.centerx - self.musicoff_text.get_width() // 2, self.musicoff_rect.centery - self.musicoff_text.get_height() // 2))
            pygame.display.update()

    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = BUTTON_WIDTH + 20
            button_rect.h = BUTTON_HEIGHT + 10
        else:
            button_rect.w = BUTTON_WIDTH
            button_rect.h = BUTTON_HEIGHT

# Quit Pygame
pygame.mixer.quit()
pygame.quit()