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
                        return "main"
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
#class for the credits
class CreditsMenu(MenuManager):
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
            "Coordination transverse : Mantoulaye MBENGUE",
            "",
            "Oiseau : Cassandre CHANDELIER",
            "",
            "Design background : Letícia AIRES",
            "",
            "Runner : Letícia AIRES",
            "",
            "Obstacles aléatoires quantiques : Solène CERPAC et Zineb LAHMOUDI",
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
                            return "main"
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


#class for the game : History Mode
class Game:

    """
    Game Loop
        - run
        - events
        - update
        - quit_game
    """

    def __init__(self):

        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.font.init()
        self.FPS = 80
        self.clock = pygame.time.Clock()

        # Indique si l'asset doit descendre
        self.move = False

        self.gapx = 100
        self.gapy = 500

        self.new()
        self.load()

        self.playing = True


    def new(self):
        self.project_tile = "Flappy"
        pygame.display.set_caption(self.project_tile)

        self.gameDisplay = pygame.display.set_mode((450,504))
        self.image = pygame.image.load('assets/fond.png')

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        # Definition sprite oiseau
        self.image_bird = pygame.image.load('assets/birdy.png')
        self.bird_real = pygame.transform.scale(self.image_bird, (
        self.image_bird.get_width() // 10, self.image_bird.get_height() // 10))

        # Definition des bords du sprite oiseau
        self.rect_bird = self.image.get_rect()
        self.rect_bird.x = 150
        self.rect_bird.y = 250

        # Récupération asset tuyau
        self.image_pipe = pygame.image.load('assets/tuyau_final.png')
        self.pipe_inv = pygame.transform.scale(self.image_pipe, (
            self.image_pipe.get_width(), self.image_pipe.get_height()))

        # Position premier tuyau
        self.pos = [300]
        self.rect_pipe = self.image_pipe.get_rect()
        self.rect_pipe.x = 300
        self.rect_pipe.y = 302


        # Ce qu'on veut inverser
        self.inverser_horizontalement = False
        self.inverser_verticalement = True

        # Inversion
        self.image_inversee = pygame.transform.flip(self.pipe_inv, self.inverser_horizontalement,
                                                    self.inverser_verticalement)

    def load(self):
        self.timer = 0
        self.delay = 100
        self.map = 0
        self.map2 = 900

    def run(self):
        while self.playing:
            self.events()
            self.update()
            self.clock.tick(self.FPS)

            pygame.display.flip()

        self.quit_game_jeu()

    def events(self):
        self.event = pygame.event.get()
        for event in self.event:
            # Check for keyboard shortcuts
            if event.type == pygame.KEYDOWN:
                self.move = True
                if event.key == pygame.K_ESCAPE:
                    self.quit_game_jeu()
                elif event.key == pygame.K_SPACE:
                    if self.rect_bird.y > 15:
                        self.rect_bird.y -= 30
            # Handle quit event
            if event.type == pygame.QUIT:
                self.quit_game_jeu()

    def update(self):

        if self.timer <= 0:
            self.timer = self.delay
            self.map -= 1  # Déplacement vers la gauche
            self.map2 -= 1
            # Si la première image sort complètement de l'écran, replacez-la à droite de la seconde image
            if self.map < -900:
                self.map = self.map2 + 900
            # Si la seconde image sort complètement de l'écran, replacez-la à droite de la première image
            if self.map2 < - 900:
                self.map2 = self.map + 900

            if self.move:
                if self.rect_bird.y <= 450:
                    self.rect_bird.y += 2  # Descendre de 2 pixels

                if self.rect_pipe.x <=350:
                    self.rect_pipe.x -= 2  # Descendre de 2 pixels à gauche
        else:
            self.timer -= 50

        # map
        self.gameDisplay.blit(self.image, (self.map, self.rect.y))
        self.gameDisplay.blit(self.image, (self.map2, self.rect.y))
        # oiseau
        self.gameDisplay.blit(self.bird_real, (self.rect_bird.x, self.rect_bird.y))
        # tuyau
        self.gameDisplay.blit(self.image_pipe, (self.rect_pipe.x, self.rect_pipe.y))
        self.gameDisplay.blit(self.image_inversee, (self.rect_pipe.x, self.rect_pipe.y - self.gapy))

    def draw(self):
        pass

    def quit_game_jeu(self):
        quit()











# Run the main menu
if __name__ == "__main__":
    menu = MainMenu()
    running = True
    while running:
        # Check the current menu screen state
        current_menu = menu.run()
        # Act based on the menu the user returns from
        if current_menu == "main":
            menu = MainMenu()
        elif current_menu == "settings":
            menu = SettingMenu()
        # Add other menu states as needed
        else:
            running = False  # If the user decides to quit the game

    # Quit Pygame
    pygame.mixer.quit()
    pygame.quit()