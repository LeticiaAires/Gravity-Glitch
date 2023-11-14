import pygame
pygame.init()
import sys

import random
rnd = random.Random()

BLACK = (0, 0, 0)

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

        self.tuyauy = 300
        self.gapy = 500

        self.pas = 0

        self.aleatoire = 0

        self.new()
        self.load()

        self.playing = True


    def new(self):
        self.project_tile = "Flappy"
        pygame.display.set_caption(self.project_tile)

        self.gameDisplay = pygame.display.set_mode((800,500))
        self.image = pygame.image.load('assets/fond.png')

        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        # Definition sprite oiseau
        self.image_bird = pygame.image.load('assets/birdy.png')
        self.bird_real = pygame.transform.scale(self.image_bird,(self.image_bird.get_width()//10, self.image_bird.get_height() // 10))



        #print(self.image_bird.get_width()//10)
        #print(self.image_bird.get_height()//10)

        # Position du sprite oiseau et des bords
        self.rect_bird = self.bird_real.get_rect()
        self.rect_bird.x = 150
        self.rect_bird.y = 250

        # Récupération asset tuyau
        self.image_pipe = pygame.image.load('assets/tuyau_final.png')
        self.pipe_inv = pygame.transform.scale(self.image_pipe, (
            self.image_pipe.get_width(), self.image_pipe.get_height()))


        # Ce qu'on veut inverser
        self.inverser_horizontalement = False
        self.inverser_verticalement = True

        # Inversion
        self.image_inversee = pygame.transform.flip(self.pipe_inv, self.inverser_horizontalement,
                                                    self.inverser_verticalement)


        # Position du tuyau
        self.rect_pipe = self.pipe_inv.get_rect()
        self.rect_pipe.x = 300
        self.rect_pipe.y = 300

        # Position premier tuyau
        self.pos = 300
        self.pos2 = self.pos + 300  # tuyau suivant
        self.pos3 = self.pos2 + 300

        # Valeurs aléatoires pour les tuyaux (hauteur)
        self.alt = rnd.randint(200, 400)
        self.alt2 = rnd.randint(200, 400)
        self.alt3 = rnd.randint(200, 400)

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

            if self.rect_bird.colliderect(self.rect_pipe):
                print("Collision détectée !")

            # Handle quit event
            if event.type == pygame.QUIT:
                self.quit_game_jeu()



    def update(self):

        if self.timer <= 0:
            self.timer = self.delay
            self.map -= 1  # Déplacement vers la gauche
            self.map2 -= 1

            # Si la première image sort complètement de l'écran, on remplace à droite par la seconde image
            if self.map < -900:
                self.map = self.map2 + 900
                self.pas += 1
                print(self.pas)
            # Si la seconde image sort complètement de l'écran, on remplace à droite par la première image
            if self.map2 < - 900:
                self.map2 = self.map + 900


            if self.move:
                if self.rect_bird.y <= 450:
                    self.rect_bird.y += 2  # Descendre de 2 pixels

                if self.pos <=-100:
                    self.pos = 800
                    self.aleatoire = rnd.randint(-100, 100)
                    self.alt = self.tuyauy + self.aleatoire

                if self.pos2 <=-100:
                    self.pos2 = 800
                    self.aleatoire = rnd.randint(-100, 100)
                    self.alt2 = self.tuyauy + self.aleatoire

                if self.pos3 <=-100:
                    self.pos3 = 800
                    self.aleatoire = rnd.randint(-100, 100)
                    self.alt3 = self.tuyauy + self.aleatoire


                self.pos -= 2  # Descendre de 2 pixels à gauche
                self.pos2 -= 2
                self.pos3 -= 2


        else:
            self.timer -= 60

        # map
        self.gameDisplay.blit(self.image, (self.map, self.rect.y))
        self.gameDisplay.blit(self.image, (self.map2, self.rect.y))
        # oiseau
        self.gameDisplay.blit(self.bird_real, (self.rect_bird.x, self.rect_bird.y))

        # tuyau
        self.gameDisplay.blit(self.image_pipe, (self.pos, self.alt ))
        self.gameDisplay.blit(self.image_inversee, (self.pos, self.alt - self.gapy ))

        self.gameDisplay.blit(self.image_pipe, (self.pos2, self.alt2 ))
        self.gameDisplay.blit(self.image_inversee, (self.pos2, self.alt2 - self.gapy))

        self.gameDisplay.blit(self.image_pipe, (self.pos3, self.alt3 ))
        self.gameDisplay.blit(self.image_inversee, (self.pos3, self.alt3 - self.gapy))

    def draw(self):
        pass

    def quit_game_jeu(self):
        pygame.quit()
        quit()


game = Game()

running = True

while running:
    game.run()
