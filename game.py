import pygame
pygame.init()

BLACK = (0, 0, 0)


class Game:
    """
    Initialization
    """
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.font.init()
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.playing = True
        self.new()
        self.load()


    def new(self):
        self.project_tile = "Flappy"
        pygame.display.set_caption(self.project_tile)
        self.gameDisplay = pygame.display.set_mode((450,504))
        self.background = pygame.image.load('assets/fond_flappy.png')

    def load(self):
        self.timer = 0
        self.delay = 100
        self.map = 0
        self.map2 = 0
        self.inf = 0

    """
    Game Loop
        - run
        - events
        - update
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

            if self.map == -900:
                self.map = 450
                self.inf += 1

            else:
                self.map -= 5
                print(self.map)
                self.gameDisplay.blit(self.background, (self.map, 0 + self.inf * 10))

                if self.map > -900 or self.map <0:
                    self.gameDisplay.blit(self.background, (self.map+900, 0 + self.inf * 10))

        else:
            self.timer -= 90

        pygame.display.flip()






    def draw(self):
        pass
    def quit_game(self):
        pygame.quit()
        quit()



game = Game()

running = True

while running:
    game.run()

    """
            if self.map == -900:
                self.map = 450
                self.inf += 1


            elif self.timer <= 0:
                self.map -= 10
                print(self.map)

                self.gameDisplay.blit(self.background, (self.map, 0 + self.inf * 10))
                if self.map < -450:
                    self.gameDisplay.blit(self.background, (self.map + 900, 0 + self.inf *10))

            else:
                self.timer -= 100
    """