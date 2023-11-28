import os
import pygame
import sys
import random
rnd = random.Random()



from MenuManager import MenuManager  # Importation de la classe parente MenuManager depuis le fichier MenuManager.py



# the class for the main menu
class MainMenu(MenuManager):
    def __init__(self):
        super().__init__()# Appel du constructeur de la classe parente
        self.title_font = pygame.font.Font(self.font_path, 50)
        self.button_font = pygame.font.Font(self.font_path, 36)

        self.play_button = self.button_font.render("Play", True, self.class_BLACK)
        self.play_rect = pygame.Rect((self.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2, 100, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        
        self.rules_button = self.button_font.render("Rules", True, (0, 0, 0))
        self.rules_rect = pygame.Rect((self.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2, 200, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        
        self.credits_button = self.button_font.render("Credits", True, (0, 0, 0))
        self.credits_rect = pygame.Rect((self.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2, 300, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        
        self.setting_button = self.button_font.render("Settings", True, (0, 0, 0))
        self.setting_rect = pygame.Rect((self.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2, 400, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        
        self.quit_button = self.button_font.render("Quit", True, (0,0,0))
        self.quit_rect = pygame.Rect((self.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2, 500, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

    def run(self):
        running = True
        from PseudoChoice import NameMenu
        from Rules import RulesMenu
        from Credits import CreditsMenu
        from Settings import SettingMenu
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.play_rect.collidepoint(mouse_pos):
                        print("The button 'Play' has been pressed")
                        name_menu = NameMenu()
                        name_menu.run()
                    elif self.rules_rect.collidepoint(mouse_pos):
                        print("The button 'Rules' has been pressed")
                        rules_menu=RulesMenu()
                        rules_menu.run()
                    elif self.credits_rect.collidepoint(mouse_pos):
                        print("The button 'Credits' has been pressed")
                        credits_menu = CreditsMenu()
                        credits_menu.run()
                    elif self.setting_rect.collidepoint(mouse_pos):
                        print("The button 'Settings' has been pressed")
                        setting_menu = SettingMenu()
                        setting_menu.run()
                    elif self.quit_rect.collidepoint(mouse_pos):
                        print("The button 'Quit' has been pressed")
                        running = False
                        print("Goodbye!")
                        return "quit"
                        
                        

                mouse_pos = pygame.mouse.get_pos()
                self.update_button(self.play_rect, self.play_button, mouse_pos)
                self.update_button(self.rules_rect, self.rules_button, mouse_pos)
                self.update_button(self.credits_rect, self.credits_button, mouse_pos)
                self.update_button(self.setting_rect, self.setting_button, mouse_pos)
                self.update_button(self.quit_rect, self.quit_button, mouse_pos)

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_font.render("Welcome to Gravity Glitch", True, (255,255,255)), (self.SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.play_button, (self.play_rect.centerx - self.play_button.get_width() // 2, self.play_rect.centery - self.play_button.get_height() // 2))
            self.screen.blit(self.rules_button, (self.rules_rect.centerx - self.rules_button.get_width() // 2, self.rules_rect.centery - self.rules_button.get_height() // 2))
            self.screen.blit(self.credits_button, (self.credits_rect.centerx - self.credits_button.get_width() // 2, self.credits_rect.centery - self.credits_button.get_height() // 2))
            self.screen.blit(self.setting_button, (self.setting_rect.centerx - self.setting_button.get_width() // 2, self.setting_rect.centery - self.setting_button.get_height() // 2))
            self.screen.blit(self.quit_button, (self.quit_rect.centerx - self.quit_button.get_width() // 2, self.quit_rect.centery - self.quit_button.get_height() // 2))

            pygame.display.update()
        
        

    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT


