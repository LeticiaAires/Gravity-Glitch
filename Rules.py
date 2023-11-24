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

#class for the rules
class RulesMenu(MenuManager):
    def __init__(self):
        super().__init__()
        self.title_rules_font = pygame.font.Font(font_path, 50)
        self.title_rules_text = self.title_rules_font.render("Rules", True, (255, 255, 255))
        self.title_rules_rect = self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

        self.return_font = pygame.font.Font(font_path, 30)
        self.return_button = self.return_font.render("Return", True, (20,20,20))
        self.return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 6, 500, BUTTON_WIDTH, BUTTON_HEIGHT)

        self.rules_font = pygame.font.Font(font_path, 20)
        #rules for the history mode
        self.rules_text=self.rules_font.render("Try to get the bird through as many holes as possible" ,True, (0,0,0))
        self.rules_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.rules0_text=self.rules_font.render("For the history mode : " ,True, (0,0,0))
        self.rules0_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.rules2_text=self.rules_font.render("If you hit the pipes the game is over !" ,True, (0,0,0))
        self.rules2_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.rules3_text=self.rules_font.render("To play, push the space bar or use the console" ,True, (0,0,0))
        self.rules3_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        #rules for the reverse mode 
        self.rules6_text=self.rules_font.render("For the reverse mode : " ,True, (0,0,0))
        self.rules6_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.rules7_text=self.rules_font.render("Get through as many pipes as possible" ,True, (0,0,0))
        self.rules7_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.rules8_text=self.rules_font.render("If you go through a blank space the game is over !" ,True, (0,0,0))
        self.rules8_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        #choose name, character
        self.rules4_text=self.rules_font.render("First choose your name and character" ,True, (0,0,0))
        self.rules4_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.rules5_text=self.rules_font.render("Then Pick your game mode !" ,True, (0,0,0))
        self.rules5_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))


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
            self.screen.blit(self.title_rules_text, (SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.rules0_text, (SCREEN_WIDTH // 2 - 260, 200))
            self.screen.blit(self.rules4_text, (SCREEN_WIDTH // 2 - 300, 100))
            self.screen.blit(self.rules5_text, (SCREEN_WIDTH // 2 - 300, 140))
            self.screen.blit(self.rules_text, (SCREEN_WIDTH // 2 - 300, 240))
            self.screen.blit(self.rules2_text, (SCREEN_WIDTH // 2 - 300, 280))
            self.screen.blit(self.rules3_text, (SCREEN_WIDTH // 2 - 300, 320))
            self.screen.blit(self.rules6_text, (SCREEN_WIDTH // 2 - 260, 380))
            self.screen.blit(self.rules7_text, (SCREEN_WIDTH // 2 - 300, 420))
            self.screen.blit(self.rules8_text, (SCREEN_WIDTH // 2 - 300, 460))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
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