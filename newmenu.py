import os
import pygame
import sys

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 60

# Define the font file and path
font_filename = "your_font.ttf"
font_path = os.path.join("Assets", font_filename)

# Create a class to manage the menu screens
class MenuManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Menu Gravity Glitch")
        self.background_image = pygame.image.load("Assets/background2.jpg").convert()
        self.background_rect = self.background_image.get_rect()

    def run(self):
        pass

# Create a class for the main menu
class MainMenu(MenuManager):
    def __init__(self):
        super().__init__()
        self.title_font = pygame.font.Font(font_path, 50)
        self.button_font = pygame.font.Font(font_path, 36)

        self.play_button = self.button_font.render("Play", True, (0, 0, 0))
        self.play_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 100, BUTTON_WIDTH, BUTTON_HEIGHT)
        
        self.rules_button = self.button_font.render("Rules", True, (0, 0, 0))
        self.rules_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT)
        
        self.credits_button = self.button_font.render("Credits", True, (0, 0, 0))
        self.credits_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)
        
        self.setting_button = self.button_font.render("Settings", True, (0, 0, 0))
        self.setting_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT)
        
        self.quit_button = self.button_font.render("Quit", True, (0, 0, 0))
        self.quit_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 500, BUTTON_WIDTH, BUTTON_HEIGHT)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.play_rect.collidepoint(mouse_pos):
                        print("The button 'Play' has been pressed")
                        game_menu = GameMenu()
                        game_menu.run()
                    elif self.rules_rect.collidepoint(mouse_pos):
                        print("The button 'Rules' has been pressed")
                    elif self.credits_rect.collidepoint(mouse_pos):
                        print("The button 'Credits' has been pressed")
                    elif self.setting_rect.collidepoint(mouse_pos):
                        print("The button 'Settings' has been pressed")
                        setting_menu = SettingMenu()
                        setting_menu.run()
                    elif self.quit_rect.collidepoint(mouse_pos):
                        print("The button 'Quit' has been pressed")
                        running = False
                        print("Goodbye!")

                mouse_pos = pygame.mouse.get_pos()
                self.update_button(self.play_rect, self.play_button, mouse_pos)
                self.update_button(self.rules_rect, self.rules_button, mouse_pos)
                self.update_button(self.credits_rect, self.credits_button, mouse_pos)
                self.update_button(self.setting_rect, self.setting_button, mouse_pos)
                self.update_button(self.quit_rect, self.quit_button, mouse_pos)

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_font.render("Welcome to Gravity Glitch", True, (0, 0, 0)), (SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.play_button, (self.play_rect.centerx - self.play_button.get_width() // 2, self.play_rect.centery - self.play_button.get_height() // 2))
            self.screen.blit(self.rules_button, (self.rules_rect.centerx - self.rules_button.get_width() // 2, self.rules_rect.centery - self.rules_button.get_height() // 2))
            self.screen.blit(self.credits_button, (self.credits_rect.centerx - self.credits_button.get_width() // 2, self.credits_rect.centery - self.credits_button.get_height() // 2))
            self.screen.blit(self.setting_button, (self.setting_rect.centerx - self.setting_button.get_width() // 2, self.setting_rect.centery - self.setting_button.get_height() // 2))
            self.screen.blit(self.quit_button, (self.quit_rect.centerx - self.quit_button.get_width() // 2, self.quit_rect.centery - self.quit_button.get_height() // 2))

            pygame.display.update()

        pygame.mixer.quit()
        pygame.quit()

    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = BUTTON_WIDTH + 20
            button_rect.h = BUTTON_HEIGHT + 10
        else:
            button_rect.w = BUTTON_WIDTH
            button_rect.h = BUTTON_HEIGHT

# Create a class for the settings menu
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
                        main_menu = MainMenu()
                        main_menu.run()
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

# Create a class for the game menu
class GameMenu(MenuManager):
    def __init__(self):
        super().__init__()
        self.title_play_font = pygame.font.Font(font_path, 50)
        self.title_play_text = self.title_play_font.render("Play Menu", True, (255, 255, 255))
        self.title_play_rect = self.title_play_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

        self.return_font = pygame.font.Font(font_path, 30)
        self.return_button = self.return_font.render("Return", True, (0, 0, 0))
        self.return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 6, 500, BUTTON_WIDTH, BUTTON_HEIGHT)

        self.play_font = pygame.font.Font(font_path, 40)
        self.historymode_text = self.play_font.render("History Mode", True, (0, 0, 0))
        self.creationmode_text = self.play_font.render("Creation Mode", True, (0, 0, 0))

        self.historymode_rect = self.historymode_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
        self.creationmode_rect = self.creationmode_text.get_rect(center=(SCREEN_WIDTH // 2, 300))

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
                        main_menu = MainMenu()
                        main_menu.run()
                    elif self.historymode_rect.collidepoint(mouse_pos):
                        print("The button 'History Mode' has been pressed")
                    elif self.creationmode_rect.collidepoint(mouse_pos):
                        print("The button 'Creation Mode' has been pressed")

                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
                self.update_button(self.historymode_rect, self.historymode_text, mouse_pos1)
                self.update_button(self.creationmode_rect, self.creationmode_text, mouse_pos1)

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_play_text, (SCREEN_WIDTH // 3 - 200, 30))
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

# Run the main menu
if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.run()
