import os
import pygame
import sys
import random
rnd = random.Random()

from MenuManager import MenuManager  # Importation de la classe parente MenuManager depuis le fichier MenuManager.py
from ModeChoice import ModeMenu
#from Custom import CustomMenu


# class for the first page of the play menu aka Name Menu
class NameMenu(MenuManager):
    def __init__(self): 
        super().__init__()
        self.title_play_font = pygame.font.Font(MenuManager.font_path, 50)
        self.title_play_text = self.title_play_font.render("Pseudo Menu ", True, (255, 255, 255))
        self.title_play_rect = self.title_play_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 50))

        self.title2_play_font = pygame.font.Font(MenuManager.font_path, 25)
        self.title2_play_text = self.title2_play_font.render("Click on the box and enter your name  ! ", True, (0,0,0))
        self.title2_play_rect = self.title2_play_text.get_rect(center=(180, 150))

        self.title3_play_text=self.title2_play_font.render(" ", True, (0,0,0))

        #return button
        self.return_font = pygame.font.Font(MenuManager.font_path, 30)
        self.return_button = self.return_font.render("Return ", True, (0, 0, 0))
        self.return_rect = pygame.Rect((MenuManager.SCREEN_WIDTH - MenuManager.BUTTON_WIDTH) // 8, 500, MenuManager.BUTTON_WIDTH, MenuManager.BUTTON_HEIGHT)

        #continue button
        self.continue_font = pygame.font.Font(MenuManager.font_path, 30)
        self.continue_button = self.continue_font.render("Continue ", True, (0, 0, 0))
        self.continue_rect = pygame.Rect((MenuManager.SCREEN_WIDTH - MenuManager.BUTTON_WIDTH) - 100, 500, MenuManager.BUTTON_WIDTH, MenuManager.BUTTON_HEIGHT)
        
        #Init where the player will right his/her name 
        self.input_box = pygame.Rect(140, 240, 450, 100)
        self.player_name = " "
        self.active = False

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.return_rect.collidepoint(mouse_pos):
                        print("The button 'Return' has been pressed")
                        running = False
                        return "main"
                    elif self.continue_rect.collidepoint(mouse_pos):
                        print("The button 'Continue' has been pressed")
                        #custom =CustomMenu()
                        #custom.run()
                    elif self.input_box.collidepoint(mouse_pos):
                        self.active = not self.active #toggles the active state of the input box
                elif event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key==pygame.K_RETURN:
                            print(self.player_name)
                            #self.player_name=""  i commented this because it didnt keep the display of the user's name
                        elif event.key==pygame.K_BACKSPACE:
                            self.player_name=self.player_name[:-1]
                        else:
                            self.player_name+=event.unicode
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
                self.update_button(self.continue_rect, self.continue_button, mouse_pos1)
            self.screen.blit(self.background_image, (0, 0))
            self.pseudo_copy = self.title2_play_font.render(self.player_name, True, (0,0,0))
            self.screen.blit(self.title2_play_font.render("Your pseudo is " + self.player_name, True, (0, 0, 0)), ((MenuManager.SCREEN_WIDTH // 3 - 250, 400)))
            self.screen.blit(self.title_play_text, (MenuManager.SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.title2_play_text, (MenuManager.SCREEN_WIDTH // 3 - 250, 110))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
            self.screen.blit(self.continue_button, (self.continue_rect.centerx - self.continue_button.get_width() // 2, self.continue_rect.centery - self.continue_button.get_height() // 2))
            pygame.draw.rect(self.screen, (255,255,255), self.input_box, 10)
            self.title3_play_text = self.title2_play_font.render(" " + self.player_name, True, (0, 0, 0))
            self.screen.blit(self.title3_play_text, (self.input_box.x + 5, self.input_box.y + 30))      
            pygame.display.update()
#Function to increase the size of a button when the mouse is on it 
    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT
