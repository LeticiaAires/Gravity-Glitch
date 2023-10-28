import pygame
import os

pygame.init()

clock = pygame.time.Clock()
fps = 60

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Gravity Glitch')

# Define the font file and path
font_filename = "your_font.ttf"
font_path = os.path.join("Assets/your_font.ttf", font_filename)
run = True

# Define game variables
scroll_speed = 4
ground_scroll = 0

# Load images
BG = pygame.image.load("Assets/background2.jpg")


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'Assets/bird{num}.png')
            self.images.append(img)
        self.image = pygame.image.load('Assets/bird1.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.counter += 1
        flap_cooldown = 5

        if self.counter < flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]


bird_group = pygame.sprite.Group()
flappy = Bird(100, int(SCREEN_HEIGHT/2))
bird_group.add(flappy)

while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Update bird position
    flappy.rect.y += 1  # Move the bird down (you can change this to make it move up or respond to user input)

    # Scroll the background
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > SCREEN_WIDTH:
        ground_scroll = 0

    # Draw background
    screen.blit(BG, (ground_scroll, 0))

    # Draw bird and update its animation
    bird_group.update()
    bird_group.draw(screen)

    pygame.display.update()

pygame.quit()
