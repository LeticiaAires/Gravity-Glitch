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

#font file and path
font_filename = "your_font.ttf"
font_path = os.path.join("Assets", font_filename)

# the lass to manage the menu screens
class MenuManager:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Menu Gravity Glitch")
        self.background_image = pygame.image.load("Assets/background2.jpg").convert()
        self.background_rect = self.background_image.get_rect()

    def run(self):
        pass

# the class for the main menu
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
        
        self.quit_button = self.button_font.render("Quit", True, (0,0,0))
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
                        

                mouse_pos = pygame.mouse.get_pos()
                self.update_button(self.play_rect, self.play_button, mouse_pos)
                self.update_button(self.rules_rect, self.rules_button, mouse_pos)
                self.update_button(self.credits_rect, self.credits_button, mouse_pos)
                self.update_button(self.setting_rect, self.setting_button, mouse_pos)
                self.update_button(self.quit_rect, self.quit_button, mouse_pos)

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_font.render("Welcome to Gravity Glitch", True, (255,255,255)), (SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.play_button, (self.play_rect.centerx - self.play_button.get_width() // 2, self.play_rect.centery - self.play_button.get_height() // 2))
            self.screen.blit(self.rules_button, (self.rules_rect.centerx - self.rules_button.get_width() // 2, self.rules_rect.centery - self.rules_button.get_height() // 2))
            self.screen.blit(self.credits_button, (self.credits_rect.centerx - self.credits_button.get_width() // 2, self.credits_rect.centery - self.credits_button.get_height() // 2))
            self.screen.blit(self.setting_button, (self.setting_rect.centerx - self.setting_button.get_width() // 2, self.setting_rect.centery - self.setting_button.get_height() // 2))
            self.screen.blit(self.quit_button, (self.quit_rect.centerx - self.quit_button.get_width() // 2, self.quit_rect.centery - self.quit_button.get_height() // 2))

            pygame.display.update()

        pygame.mixer.quit()
        

    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = BUTTON_WIDTH + 20
            button_rect.h = BUTTON_HEIGHT + 10
        else:
            button_rect.w = BUTTON_WIDTH
            button_rect.h = BUTTON_HEIGHT

# class for the settings menu
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

# class for the play menu
class GameMenu(MenuManager):
    def __init__(self): #Here Creation stands for the inverse mode
        super().__init__()
        self.title_play_font = pygame.font.Font(font_path, 50)
        self.title_play_text = self.title_play_font.render("Play Menu", True, (255, 255, 255))
        self.title_play_rect = self.title_play_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

        self.title2_play_font = pygame.font.Font(font_path, 40)
        self.title2_play_text = self.title2_play_font.render("Enter your name ! ", True, (0,0,0))
        self.title2_play_rect = self.title2_play_text.get_rect(center=(SCREEN_WIDTH // 3, 40))

        self.return_font = pygame.font.Font(font_path, 30)
        self.return_button = self.return_font.render("Return", True, (0, 0, 0))
        self.return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 8, 500, BUTTON_WIDTH, BUTTON_HEIGHT)

        #self.play_font = pygame.font.Font(font_path, 30)
        #self.historymode_text = self.play_font.render("History Mode", True, (0, 0, 0))
        #self.creationmode_text = self.play_font.render("Inverse Mode", True, (0, 0, 0))

        #self.historymode_rect = self.historymode_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
        #self.creationmode_rect = self.creationmode_text.get_rect(center=(SCREEN_WIDTH // 2, 400))

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
                    #elif self.historymode_rect.collidepoint(mouse_pos):
                        #print("The button 'History Mode' has been pressed")
                    #elif self.creationmode_rect.collidepoint(mouse_pos):
                        #print("The button 'Inverse Mode' has been pressed")

                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
                #self.update_button(self.historymode_rect, self.historymode_text, mouse_pos1)
                #self.update_button(self.creationmode_rect, self.creationmode_text, mouse_pos1)

            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_play_text, (SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.title2_play_text, (SCREEN_WIDTH // 2 -250, 150))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
            #self.screen.blit(self.historymode_text, (self.historymode_rect.centerx - self.historymode_text.get_width() // 2, self.historymode_rect.centery - self.historymode_text.get_height() // 2))
            #self.screen.blit(self.creationmode_text, (self.creationmode_rect.centerx - self.creationmode_text.get_width() // 2, self.creationmode_rect.centery - self.creationmode_text.get_height() // 2))
            pygame.display.update()

    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = BUTTON_WIDTH + 20
            button_rect.h = BUTTON_HEIGHT + 10
        else:
            button_rect.w = BUTTON_WIDTH
            button_rect.h = BUTTON_HEIGHT
#class for the credits
class CreditsMenu:
    def __init__(self):
        super().__init__()
        # Paramètres d'affichage
        self.fenetre = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Crédits")

        # Chargement de l'image de fond
        self.fond = pygame.image.load('Assets/background2.jpg')

        # Liste de crédits
        self.credits = [
            "Développeuses : Mantoulaye MBENGUE, Solène CERPAC, Letícia AIRES, ​",
            "                       Cassandre CHANDELIER, Zineb LAHMOUDI",
            "",
            "",
            "Menu : Mantoulaye MBENGUE",
            "",
            "Choix musical : Mantoulaye MBENGUE",
            "",
            "Oiseau : Cassandre CHANDELIER",
            "",
            "Design background : Letícia AIRES",
            "",
            "Runner : Letícia AIRES",
            "",
            "Obstacles aléatoires quantiques : Solène CERPAC",
            "",
            "Obstacles aléatoires quantiques : Zineb LAHMOUDI",
            "",
            "Crédits : Solène CERPAC",
            "",
            "Testeur de jeu : Nicolas Papazoglou",
            "",
            "Testeur de jeu : Laurent Fiack",
            "",
            "Musique : Clement Panchout 'Life is full of Joy'"
        ]

        self.bouton_retour = pygame.Rect(600, 300, 200, 50)
        self.font_filename = "your_font.ttf"
        self.font_path = os.path.join("Assets", font_filename)
        self.button_font = pygame.font.Font(font_path, 20)

        self.y_position = SCREEN_HEIGHT
        self.return_font = pygame.font.Font(font_path, 30)
        self.bouton_retour = self.return_font.render("Return", True, (255,255,255))
        self.return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 1, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.defilement_actif = True
    def run(self):
            bouton_retour = self.bouton_retour
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        print("Mouse pos : "+ str(mouse_pos))
                        print(str(bouton_retour))
                        print(str(self.return_rect.collidepoint(mouse_pos)))
                        if self.return_rect.collidepoint(mouse_pos):
                            # L'utilisateur a cliqué sur le bouton "Retour"
                            running = False
                            main_menu = MainMenu()
                            main_menu.run()
                self.fenetre.blit(self.fond, (0, 0))
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.bouton_retour, mouse_pos1)
                if self.defilement_actif:
                    for i, ligne in enumerate(self.credits):
                        texte = self.button_font.render(ligne, True, (0, 0, 0))
                        y = self.y_position + i * 40
                        self.fenetre.blit(texte, (40, y))

                    self.y_position -= 0.2

                    if self.y_position < -len(self.credits) * 45:
                        defilement_actif = False

                self.fenetre.blit(self.bouton_retour, (self.return_rect.centerx - self.bouton_retour.get_width() // 2, self.return_rect.centery - self.bouton_retour.get_height() // 2))
                #if not defilement_actif:
                    #credits_button = button_font.render("Menu", True, (0, 0, 0))
                    #credits_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)
                    #pygame.draw.rect(fenetre, (255, 255, 255), credits_rect)
                    #text_x = credits_rect.x + (credits_rect.width - credits_button.get_width()) // 2
                    #text_y = credits_rect.y + (credits_rect.height - credits_button.get_height()) // 2
                    #fenetre.blit(credits_button, (text_x, text_y))
                pygame.display.update()
                pygame.display.flip() 
    
    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = BUTTON_WIDTH + 20
            button_rect.h = BUTTON_HEIGHT + 10
        else:
            button_rect.w = BUTTON_WIDTH
            button_rect.h = BUTTON_HEIGHT   
    
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
        self.rules_text=self.rules_font.render("Try to get the bird through as many holes as possible" ,True, (0,0,0))
        self.rules_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.rules2_text=self.rules_font.render("If you hit the pipes the game is over" ,True, (255, 255, 255))
        self.rules2_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))
        self.rules3_text=self.rules_font.render("To play, push the space bar or use the console" ,True, (0,0,0))
        self.rules3_rect=self.title_rules_text.get_rect(center=(SCREEN_WIDTH // 2, 20))

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
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
           
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.title_rules_text, (SCREEN_WIDTH // 3 - 200, 30))
            self.screen.blit(self.rules_text, (SCREEN_WIDTH // 2 - 300, 200))
            self.screen.blit(self.rules_text, (SCREEN_WIDTH // 2 - 300, 300))
            self.screen.blit(self.rules_text, (SCREEN_WIDTH // 2 - 300, 400))
            self.screen.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
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
pygame.quit()