import os
import pygame
import sys
import random
rnd = random.Random()

from MenuManager import MenuManager  # Importation de la classe parente MenuManager depuis le fichier MenuManager.py

#class for the rules
class RulesMenu(MenuManager):
    def __init__(self):
        super().__init__()
        self.title_rules_font = pygame.font.Font(self.font_path, 50)
        self.title_rules_text = self.title_rules_font.render("Rules", True, MenuManager.class_WHITE)
        self.title_rules_rect = self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 50))

        self.return_font = pygame.font.Font(MenuManager.font_path, 30)
        self.return_button = self.return_font.render("Return", True, (20,20,20))
        self.return_rect = pygame.Rect((MenuManager.SCREEN_WIDTH - MenuManager.BUTTON_WIDTH) // 6, 500, MenuManager.BUTTON_WIDTH, MenuManager.BUTTON_HEIGHT)

        self.rules_font = pygame.font.Font(MenuManager.font_path, 20)
        #rules for the history mode
        self.rules_text=self.rules_font.render("Try to get the bird through as many holes as possible" ,True, MenuManager.class_BLACK)
        self.rules_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        self.rules0_text=self.rules_font.render("For the history mode : " ,True, MenuManager.class_BLACK)
        self.rules0_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        self.rules2_text=self.rules_font.render("If you hit the pipes the game is over !" ,True, MenuManager.class_BLACK)
        self.rules2_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        self.rules3_text=self.rules_font.render("To play, push the space bar or use the console" ,True, MenuManager.class_BLACK)
        self.rules3_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        #rules for the reverse mode 
        self.rules6_text=self.rules_font.render("For the reverse mode : " ,True, MenuManager.class_BLACK)
        self.rules6_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        self.rules7_text=self.rules_font.render("Get through as many pipes as possible" ,True, MenuManager.class_BLACK)
        self.rules7_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        self.rules8_text=self.rules_font.render("If you go through a blank space the game is over !" ,True, MenuManager.class_BLACK)
        self.rules8_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        #choose name, character
        self.rules4_text=self.rules_font.render("First choose your name and character" ,True, MenuManager.class_BLACK)
        self.rules4_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        self.rules5_text=self.rules_font.render("Then Pick your game mode !" ,True, MenuManager.class_BLACK)
        self.rules5_rect=self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 20))
        # display the rules from file 
        # file = open ("Rules.txt", "r", )


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
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)

           
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_rules_text, (MenuManager.SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.rules0_text, (MenuManager.SCREEN_WIDTH // 2 - 260, 200))
            self.screen.blit(self.rules4_text, (MenuManager.SCREEN_WIDTH // 2 - 300, 100))
            self.screen.blit(self.rules5_text, (MenuManager.SCREEN_WIDTH // 2 - 300, 140))
            self.screen.blit(self.rules_text, (MenuManager.SCREEN_WIDTH // 2 - 300, 240))
            self.screen.blit(self.rules2_text, (MenuManager.SCREEN_WIDTH // 2 - 300, 280))
            self.screen.blit(self.rules3_text, (MenuManager.SCREEN_WIDTH // 2 - 300, 320))
            self.screen.blit(self.rules6_text, (MenuManager.SCREEN_WIDTH // 2 - 260, 380))
            self.screen.blit(self.rules7_text, (MenuManager.SCREEN_WIDTH // 2 - 300, 420))
            self.screen.blit(self.rules8_text, (MenuManager.SCREEN_WIDTH // 2 - 300, 460))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
            pygame.display.update()
#Function to increase the size of a button when the mouse is on it 
    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT
