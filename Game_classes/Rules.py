import pygame
import sys
from MenuManager import MenuManager

class RulesMenu(MenuManager):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("rules")
        self.title_rules_font = pygame.font.Font(self.font_path, 50)
        self.return_font = pygame.font.Font(MenuManager.font_path, 30)
        self.rules_font = pygame.font.Font(MenuManager.font_path, 20)

        self.title_rules_text = self.title_rules_font.render("Rules", True, MenuManager.class_WHITE)
        self.title_rules_rect = self.title_rules_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 50))

        self.return_button = self.return_font.render("Return", True, (20, 20, 20))
        self.return_rect = pygame.Rect((MenuManager.SCREEN_WIDTH - MenuManager.BUTTON_WIDTH) // 1, 500, MenuManager.BUTTON_WIDTH, MenuManager.BUTTON_HEIGHT)

        self.rules_data = [
            ("", 200, [
                "Try to get the bird through as many holes as possible",
                "If you hit the pipes the game is over!",
                "To play, push the space bar or use the console"
            ]),
       
            ("First choose your name and character", 100, [
                
            ])
        ]

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

            for rule, y_position, lines in self.rules_data:
                self.screen.blit(self.rules_font.render(rule, True, MenuManager.class_BLACK), (MenuManager.SCREEN_WIDTH // 2 - 260, y_position))
                y_position += 40
                for line in lines:
                    self.screen.blit(self.rules_font.render(line, True, MenuManager.class_BLACK), (MenuManager.SCREEN_WIDTH // 2 - 300, y_position))
                    y_position += 40

            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
            pygame.display.update()

    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT