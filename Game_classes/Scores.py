import pygame
from MenuManager import MenuManager
#a class accessed by 
class Scores(MenuManager):
    def __init__(self) :
        super().__init__
        self.screen = pygame.display.set_mode((MenuManager.SCREEN_WIDTH,MenuManager.SCREEN_HEIGHT))
        pygame.display.set_caption("Best Scores Window")
        self.background_image = pygame.image.load("Assets/pauseWindow_screen2.png").convert() #taille image : 700 et 394
        self.background_rect = self.background_image.get_rect()
        self.title_font = pygame.font.Font(MenuManager.font_path, 50)
        self.title_text = self.title_font.render("Pause", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(MenuManager.SCREEN_WIDTH // 2, 50))

        self.return_font = pygame.font.Font(MenuManager.font_path, 30)
        self.return_button = self.return_font.render("Return ", True, (0, 0, 0))
        self.return_rect = pygame.Rect((MenuManager.SCREEN_WIDTH//2),100, MenuManager.BUTTON_WIDTH, MenuManager.BUTTON_HEIGHT)
    def run(self):
        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running1 = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.return_rect.collidepoint(mouse_pos):
                        print("The 'return' button has been pressed")
                        running1=False
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_text, (MenuManager.SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2-70, self.return_rect.centery - self.return_button.get_height() // 2))
            pygame.display.update()  
#Function to increase the size of a button when the mouse is on it 
    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT

