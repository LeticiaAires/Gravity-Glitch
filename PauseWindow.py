import os
import pygame
import sys
import random
rnd = random.Random()

from MenuManager import MenuManager  # Importation de la classe parente MenuManager depuis le fichier MenuManager.py
from MainMenu import MainMenu  # Importation de la classe MainMenu depuis le fichier MainMenu.py
from settings import SettingMenu

#class for the pause window during the game 
class PauseWindow(MenuManager):
    def __init__(self):
        PLAY_SCREEN_HEIGHT = 600
        PLAY_SCREEN_WIDTH=800
        self.screen = pygame.display.set_mode((PLAY_SCREEN_WIDTH,PLAY_SCREEN_HEIGHT))
        pygame.display.set_caption("Pause Window")
        self.background_image = pygame.image.load("Assets/pauseWindow_screen2.png").convert() #taille image : 700 et 394
        self.background_rect = self.background_image.get_rect()
        self.title_setting_font = pygame.font.Font(MenuManager.font_path, 50)
        self.title_setting_text = self.title_setting_font.render("Pause", True, (255, 255, 255))
        self.title_setting_rect = self.title_setting_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 50))

        self.return_font = pygame.font.Font(MenuManager.font_path, 30)
        self.return_button = self.return_font.render("Return to Game", True, (0, 0, 0))
        self.return_rect = pygame.Rect((PLAY_SCREEN_WIDTH//2),100, MenuManager.BUTTON_WIDTH, MenuManager.BUTTON_HEIGHT)
        self.quit_text = self.return_font.render("Quit Game", True, (0, 0, 0))
        self.quit_rect = self.quit_text.get_rect(center=(PLAY_SCREEN_WIDTH // 2, 500))
        self.settings_text = self.return_font.render("Settings ", True, (0, 0, 0))
        self.restart_text = self.return_font.render("Restart ", True, (0, 0, 0))
        self.bestScores_text = self.return_font.render("Best Scores ", True, (0, 0, 0))
        self.settings_rect = self.settings_text.get_rect(center=(PLAY_SCREEN_WIDTH // 2, 200))
        self.restart_rect = self.restart_text.get_rect(center=(PLAY_SCREEN_WIDTH // 2, 300))
        self.bestScores_rect = self.bestScores_text.get_rect(center=(PLAY_SCREEN_WIDTH // 2, 400))

    def run(self):
        PLAY_SCREEN_HEIGHT = 600
        PLAY_SCREEN_WIDTH=800
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
                        return "play"
                    elif self.settings_rect.collidepoint(mouse_pos):
                        print("The button 'settings' has been pressed")
                        return "settings"
                    elif self.restart_rect.collidepoint(mouse_pos):
                        print("The button 'restart' has been pressed")
                    elif self.bestScores_rect.collidepoint(mouse_pos):
                        print("The button 'restart' has been pressed")
                    elif self.quit_rect.collidepoint(mouse_pos):
                        print("The 'quit' button has been pressed")
                        running1=False
                        return "pause"
            
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
                self.update_button(self.settings_rect, self.settings_text, mouse_pos1)
                self.update_button(self.restart_rect, self.restart_text, mouse_pos1)
                self.update_button(self.bestScores_rect, self.bestScores_text, mouse_pos1)
                self.update_button(self.quit_rect, self.quit_text, mouse_pos1)
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_setting_text, (PLAY_SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2-70, self.return_rect.centery - self.return_button.get_height() // 2))
            self.screen.blit(self.settings_text, (self.settings_rect.centerx - self.settings_text.get_width() // 2, self.settings_rect.centery - self.settings_text.get_height() // 2))
            self.screen.blit(self.restart_text, (self.restart_rect.centerx - self.restart_text.get_width() // 2, self.restart_rect.centery - self.restart_text.get_height() // 2))
            self.screen.blit(self.bestScores_text, (self.bestScores_rect.centerx - self.bestScores_text.get_width() // 2+20, self.bestScores_rect.centery - self.bestScores_text.get_height() // 2))
            self.screen.blit(self.quit_text, (self.quit_rect.centerx - self.quit_text.get_width() // 2, self.quit_rect.centery - self.quit_text.get_height() // 2))
            pygame.display.update()  
    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT


