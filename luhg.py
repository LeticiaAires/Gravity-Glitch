import pygame
import sys
import random

pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
GRAVITY = 0.25
BIRD_SPEED = -9
PIPE_SPEED = -4

# Colors
WHITE = (255, 255, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flappy Bird')

# Load assets
bg = pygame.image.load('background.jpg')
bird = pygame.image.load('bird.png')
pipe = pygame.image.load('pipe.png')

# Bird properties
bird_x = 50
bird_y = 200
bird_speed = 0
bird_rect = bird.get_rect(topleft=(bird_x, bird_y))

# Pipe properties
pipe_x = SCREEN_WIDTH
pipe_width = pipe.get_width()
pipes = []

# Game variables
game_active = True
score = 0
font = pygame.font.Font(None, 36)

# Function to draw the score on the screen
def draw_score():
    score_display = font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_display, (10, 10))

# Function to check for collisions
def collision_check():
    global game_active

    if bird_rect.bottom >= SCREEN_HEIGHT:
        game_active = False

    for pipe_rect in pipes:
        if bird_rect.colliderect(pipe_rect):
            game_active = False

# Function to update the position of pipes and handle scoring
def update_pipes():
    global pipes, score

    for pipe_rect in pipes:
        pipe_rect.centerx += PIPE_SPEED

    pipes = [pipe for pipe in pipes if pipe.right > 0]

    if pipes and bird_x > pipes[0].centerx > bird_x - PIPE_SPEED:
        score += 1

# Function to make the bird flap
def flap():
    global bird_speed
    bird_speed = BIRD_SPEED

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                flap()

    if game_active:
        bird_speed += GRAVITY
        bird_rect.centery += bird_speed

        if bird_rect.centery >= SCREEN_HEIGHT:
            bird_rect.centery = SCREEN_HEIGHT

        update_pipes()
        collision_check()

    screen.blit(bg, (0, 0))
    for pipe_rect in pipes:
        screen.blit(pipe, pipe_rect)

    screen.blit(bird, bird_rect)

    draw_score()

    if not game_active:
        game_over_surface = font.render('Game Over', True, WHITE)
        game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(game_over_surface, game_over_rect)

    pygame.display.update()
    clock.tick(60)

# Properly close the game window
pygame.quit()
sys.exit()
