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





# class for the second page of the play menu
class GameMenu2(MenuManager):
    def __init__(self): #Here Creation stands for the inverse mode
        super().__init__()
        self.title_play_font = pygame.font.Font(font_path, 50)
        self.title_play_text = self.title_play_font.render("Mode Menu", True, (255, 255, 255))
        self.title_play_rect = self.title_play_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

        self.title2_play_font = pygame.font.Font(font_path, 40)
        self.title2_play_text = self.title2_play_font.render("Choose your mode ", True, (0,0,0))
        self.title2_play_rect = self.title2_play_text.get_rect(center=(SCREEN_WIDTH // 3, 40))

        self.return_font = pygame.font.Font(font_path, 30)
        self.return_button = self.return_font.render("Return", True, (0, 0, 0))
        self.return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 8, 500, BUTTON_WIDTH, BUTTON_HEIGHT)

        self.play_font = pygame.font.Font(font_path, 30)
        self.historymode_text = self.play_font.render("History Mode", True, (0, 0, 0))
        self.creationmode_text = self.play_font.render("Inverse Mode", True, (0, 0, 0))

        self.historymode_rect = self.historymode_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        self.creationmode_rect = self.creationmode_text.get_rect(center=(SCREEN_WIDTH // 2, 400))

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
                        return "main"#indicate the transition back to the menu
                    elif self.historymode_rect.collidepoint(mouse_pos):
                        print("The button 'History Mode' has been pressed")
                        game = Game()
                        game.run()
                    elif self.creationmode_rect.collidepoint(mouse_pos):
                        print("The button 'Inverse Mode' has been pressed")
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
                self.update_button(self.historymode_rect, self.historymode_text, mouse_pos1)
                self.update_button(self.creationmode_rect, self.creationmode_text, mouse_pos1)
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_play_text, (SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.title2_play_text, (SCREEN_WIDTH // 2 -250, 150))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
            self.screen.blit(self.historymode_text, (self.historymode_rect.centerx - self.historymode_text.get_width() // 2, self.historymode_rect.centery - self.historymode_text.get_height() // 2))
            self.screen.blit(self.creationmode_text, (self.creationmode_rect.centerx - self.creationmode_text.get_width() // 2, self.creationmode_rect.centery - self.creationmode_text.get_height() // 2))

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