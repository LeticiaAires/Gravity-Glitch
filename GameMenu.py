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




# class for the first page of the play menu
class GameMenu(MenuManager):
    def __init__(self): #Here Creation stands for the inverse mode
        super().__init__()
        self.title_play_font = pygame.font.Font(font_path, 50)
        self.title_play_text = self.title_play_font.render("Play Menu", True, (255, 255, 255))
        self.title_play_rect = self.title_play_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

        self.title2_play_font = pygame.font.Font(font_path, 25)
        self.title2_play_text = self.title2_play_font.render("Click on the box and enter your name  ! ", True, (0,0,0))
        self.title2_play_rect = self.title2_play_text.get_rect(center=(180, 150))

        self.title3_play_text=self.title2_play_font.render("Your name : ", True, (0,0,0))

        #return button
        self.return_font = pygame.font.Font(font_path, 30)
        self.return_button = self.return_font.render("Return", True, (0, 0, 0))
        self.return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 8, 500, BUTTON_WIDTH, BUTTON_HEIGHT)

        #continue button
        self.continue_font = pygame.font.Font(font_path, 30)
        self.continue_button = self.continue_font.render("Continue", True, (0, 0, 0))
        self.continue_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) - 100, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
        
        #Init where the player will right his/her name 
        self.input_box = pygame.Rect(140, 240, 650, 100)
        self.player_name = ""
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
                        game_menu2 = GameMenu2()
                        game_menu2.run()
                    elif self.input_box.collidepoint(mouse_pos):
                        self.active = not self.active #toggles the active state of the input box
                elif event.type == pygame.KEYDOWN:
                    if self.active:
                        if event.key==pygame.K_RETURN:
                            print(self.player_name)
                            
                            self.player_name=""
                        elif event.key==pygame.K_BACKSPACE:
                            self.player_name=self.player_name[:-1]
                        else:
                            self.player_name+=event.unicode
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
                self.update_button(self.continue_rect, self.continue_button, mouse_pos1)
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_play_text, (SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.title2_play_text, (SCREEN_WIDTH // 3 - 250, 110))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
            self.screen.blit(self.continue_button, (self.continue_rect.centerx - self.continue_button.get_width() // 2, self.continue_rect.centery - self.continue_button.get_height() // 2))
            pygame.draw.rect(self.screen, (0,0,0), self.input_box, 8)
            self.title3_play_text = self.title2_play_font.render("Your name: " + self.player_name, True, (0, 0, 0))
            self.screen.blit(self.title3_play_text, (self.input_box.x + 5, self.input_box.y + 5))          

            pygame.display.update()

    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = BUTTON_WIDTH + 20
            button_rect.h = BUTTON_HEIGHT + 10
        else:
            button_rect.w = BUTTON_WIDTH
            button_rect.h = BUTTON_HEIGHT