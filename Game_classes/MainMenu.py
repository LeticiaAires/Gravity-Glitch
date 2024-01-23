import pygame
import sys

from MenuManager import MenuManager
from PseudoChoice import NameMenu
from Rules import RulesMenu
from Credits import CreditsMenu
from Settings import SettingMenu
from Custom import CustomMenu
from Game import Start

class MainMenu(MenuManager):
    def __init__(self):
        super().__init__()
        self.title_font = pygame.font.Font(self.font_path, 50)
        self.button_font = pygame.font.Font(self.font_path, 36)

        self.button_data = [
            ("Play", 100, Start),
            ("Rules", 200, RulesMenu),
            ("Credits", 300, CreditsMenu),
            ("Personalize", 400, NameMenu),
            ("Quit", 500, sys.exit),
        ]

        self.button_actions = {}
        for idx, (text, y_position, action) in enumerate(self.button_data):
            button, rect = self.init_button(text, y_position)
            self.button_actions[idx] = {"button": button, "rect": rect, "action": action}

    def init_button(self, text, y_position):
        button = self.button_font.render(text, True, (0, 0, 0))
        rect = pygame.Rect((self.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2, y_position, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        return button, rect

    def run(self):
        running = True
        quit_flag = False

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for idx, button_info in self.button_actions.items():
                        button_rect = button_info["rect"]
                        if button_rect.collidepoint(mouse_pos):
                            button_action = button_info["action"]
                            if button_action:
                                button_action().run()
                            else:
                                print(f"The button '{button_rect}' has been pressed")

                mouse_pos = pygame.mouse.get_pos()
                self.update_button_sizes(mouse_pos)

            self.draw_menu()
            pygame.display.update()

        return quit_flag

    def update_button_sizes(self, mouse_pos):
        for button_info in self.button_actions.values():
            button_rect = button_info["rect"]
            self.update_button(button_rect, mouse_pos)

    def draw_menu(self):
        self.screen.blit(self.background_image, (0, 0))
        self.screen.blit(self.title_font.render("Welcome to Gravity Glitch", True, (255, 255, 255)), (self.SCREEN_WIDTH // 3 - 200, 30))

        for button_info in self.button_actions.values():
            button_surface = button_info["button"]
            button_rect = button_info["rect"]
            self.screen.blit(button_surface, (button_rect.centerx - button_surface.get_width() // 2, button_rect.centery - button_surface.get_height() // 2))

    def update_button(self, button_rect, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT

if __name__ == "__main__":
    pygame.init()
    menu = MainMenu()
    menu.run()
    pygame.quit()
    sys.exit()