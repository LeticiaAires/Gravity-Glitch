import pygame
import random
from pygame import *

#couleurs
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

class Game:
    """
    Initialization
    """
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.font.init()
        random.seed()
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.playing = True
        self.new()
        self.load()

    def new(self):
        self.project_tile = "Flappy"
        pygame.display.set_caption(self.project_tile)
        self.gameDisplay = pygame.display.set_mode((1080, 720))

        self.pipes = []

    def load(self):
        self.timer = 0
        self.delay = 100

    """
    Game Loop
        - run
        - events
        - update
        - draw
        - quit_game
    """
    def run(self):
        while self.playing:
            self.dt = self.clock.tick(self.FPS) / 1000
            self.events()
            self.update()
            self.draw()
        self.quit_game()

    def events(self):
        """Click: None, Left, Middle, Right, Scroll Up, Scroll Down"""
        self.click = [None, False, False, False, False, False]

        """Handle Events"""
        self.event = pygame.event.get()
        for event in self.event:
            # Check for keyboard shortcuts
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()

            # Handle quit event
            if event.type == pygame.QUIT:
                self.quit_game()

    def update(self):
        if self.timer <= 0:
            self.timer = self.delay
            position = [1080, 0]                                        #
#            size = [40, 310]                                           #
            lenght = random.randint(100, 600)                     # premier tuyau
            size = [40, lenght]                                         #

            self.pipes.append(Pipe(self.gameDisplay, position, size))

            position = [1080, lenght + 100]                             #
#           size = [40, 310]                                            # deuxième tuyau
            size = [40, 620 - lenght]                                   #

            self.pipes.append(Pipe(self.gameDisplay, position, size))

        else:
            self.timer -= 1
        for pipe in self.pipes:
            pipe.update()

        print(len(self.pipes), self.timer)

    def draw(self):
        self.gameDisplay.fill(BLUE)    ##rempli le fond en bleu

        for pipe in self.pipes:        ##parcourt la liste avec les positions/tailles des tuyaux
            pipe.draw()

        pygame.display.flip()      ##affiche

    def quit_game(self):
        pygame.quit()
        quit()


class Pipe:
    def __init__(self, gameDisplay, position, size):
        self.gameDisplay = gameDisplay
        self.position = position
        self.size = size
        self.color = GREEN
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

        self.new()
        self.load()

    def new(self):
        pass

    def load(self):
        pass

    def move(self):
        self.position[0] -= 4
        self.rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])

    def update(self):
        self.move()

    def draw(self):
        pygame.draw.rect(self.gameDisplay, self.color, self.rect)




game = Game()

running = True

while running:
    game.run()
