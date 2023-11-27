import os
import pygame
import sys
import random
rnd = random.Random()

# Initialize pygame
pygame.init()
pygame.mixer.init()

from MenuManager import MenuManager  # Importation de la classe parente MenuManager depuis le fichier MenuManager.py
from PauseWindow import PauseWindow


#class for the game : History Mode
#Things to change : augmenter la taille du jeu (image), ajouter le score, ajouter des tuyaux, ajouter musique, ajouter un bouton d'options (musique, retour, recommencer)
class Game(MenuManager):

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
        
        #Pause button
        self.pause_font = pygame.font.Font(MenuManager.font_path, 15)
        self.pause_button = self.pause_font.render("Pause", True, (0, 0, 0))
        self.pause_rect = pygame.Rect(5, 450, MenuManager.BUTTON_WIDTH, MenuManager.BUTTON_HEIGHT)

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
            if event.type == pygame.QUIT:
                self.quit_game_jeu()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.pause_rect.collidepoint(mouse_pos):
                    print("The button 'Pause' has been pressed")
                    pausemenu=PauseWindow()
                    pausemenu.run()
            # Handle quit event
            #if event.type == pygame.QUIT:
                #self.quit_game_jeu()
            mouse_pos1 = pygame.mouse.get_pos()
            self.update_button(self.pause_rect, self.pause_button, mouse_pos1)
        # Quit Pygame
        pygame.mixer.quit()
        pygame.quit()
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
        #return bouton
        self.gameDisplay.blit(self.pause_button, (self.pause_rect.centerx - self.pause_button.get_width() // 2, self.pause_rect.centery - self.pause_button.get_height() // 2))

    def draw(self):
        pass

    def quit_game_jeu(self):
        quit()

    
    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT

