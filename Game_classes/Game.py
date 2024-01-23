import os
import pygame
import random
import math
from random import randint
from collections import deque
from pygame.locals import *
import sys

from personnalizedBird import personnalisedBird

rnd = random.Random()


#class for the game : History Mode
FPS = 60
ANIMATION_SPEED = 0.18
WIN_WIDTH = 284 * 2
WIN_HEIGHT = 512


class PipePair(pygame.sprite.Sprite):

    WIDTH = 80
    PIECE_HEIGHT = 32
    ADD_INTERVAL = 3000

    def __init__(self, pipe_end_img, pipe_body_img):

        self.x = float(WIN_WIDTH - 1)
        self.score_counted = False
        self.image = pygame.Surface((PipePair.WIDTH, WIN_HEIGHT), SRCALPHA)
        self.image.convert()
        self.image.fill((0, 0, 0, 0))
        #total_pipe_body_pieces = int((WIN_HEIGHT - 3 * Bird.HEIGHT - 3 * PipePair.PIECE_HEIGHT) / PipePair.PIECE_HEIGHT)
        total_pipe_body_pieces = int((WIN_HEIGHT - 3 * personnalisedBird.HEIGHT - 3 * PipePair.PIECE_HEIGHT) / PipePair.PIECE_HEIGHT)
        self.bottom_pieces = randint(1, total_pipe_body_pieces)
        self.top_pieces = total_pipe_body_pieces - self.bottom_pieces

        for i in range(1, self.bottom_pieces + 1):

            piece_pos = (0, WIN_HEIGHT - i*PipePair.PIECE_HEIGHT)
            self.image.blit(pipe_body_img, piece_pos)
        bottom_pipe_end_y = WIN_HEIGHT - self.bottom_height_px
        bottom_end_piece_pos = (0, bottom_pipe_end_y - PipePair.PIECE_HEIGHT)
        self.image.blit(pipe_end_img, bottom_end_piece_pos)

        for i in range(self.top_pieces):

            self.image.blit(pipe_body_img, (0, i * PipePair.PIECE_HEIGHT))
        top_pipe_end_y = self.top_height_px
        self.image.blit(pipe_end_img, (0, top_pipe_end_y))
        self.top_pieces += 1
        self.bottom_pieces += 1
        self.mask = pygame.mask.from_surface(self.image)

    @property

    def top_height_px(self):
        return self.top_pieces * PipePair.PIECE_HEIGHT

    @property

    def bottom_height_px(self):
        return self.bottom_pieces * PipePair.PIECE_HEIGHT




    @property

    def visible(self):

        return -PipePair.WIDTH < self.x < WIN_WIDTH




    @property

    def rect(self):

        return Rect(self.x, 0, PipePair.WIDTH, PipePair.PIECE_HEIGHT)




    def update(self, delta_frames=1):

        self.x -= ANIMATION_SPEED * frames_to_msec(delta_frames)




    def collides_with(self, bird):

        return pygame.sprite.collide_mask(self, bird)

def load_images():

    def load_image(img_file_name):

        file_name = os.path.join(os.path.dirname(__file__), 'images', img_file_name)
        img = pygame.image.load(file_name)
        img.convert()
        return img

    return {'background': load_image('background.jpg'),
            'pipe-end': load_image('pipe_end.png'),
            'pipe-body': load_image('pipe_body.png'),
            'bird-wingup': load_image('bird_wing_up.png'),
            'bird-wingdown': load_image('bird_wing_down.png')}

def frames_to_msec(frames, fps=FPS):
    return 1000.0 * frames / fps

def msec_to_frames(milliseconds, fps=FPS):
    return fps * milliseconds / 1000.0

def game_over_screen(display_surface, score):
    font = pygame.font.SysFont(None, 48, bold=True)
    game_over_text = font.render("Game Over!", True, (255, 0, 0))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    
    quit_button = pygame.Rect(WIN_WIDTH // 2 - 75, WIN_HEIGHT // 2, 150, 50)
    reset_button = pygame.Rect(WIN_WIDTH // 2 - 75, WIN_HEIGHT // 2 + 60, 150, 50)
    menu_button = pygame.Rect(WIN_WIDTH // 2 - 75, WIN_HEIGHT // 2 + 120, 150, 50)
    
    pygame.draw.rect(display_surface, (255, 0, 0), quit_button)
    pygame.draw.rect(display_surface, (255, 0, 0), reset_button)
    pygame.draw.rect(display_surface, (255, 0, 0), menu_button)
    
    display_surface.blit(game_over_text, (WIN_WIDTH // 2 - game_over_text.get_width() // 2, WIN_HEIGHT // 4))
    display_surface.blit(score_text, (WIN_WIDTH // 2 - score_text.get_width() // 2, WIN_HEIGHT // 4 + 60))
    
    
    quit_text = font.render("Quit", True, (255, 255, 255))
    reset_text = font.render("Reset", True, (255, 255, 255))
    menu_text = font.render("Menu", True, (255, 255, 255))
    
    display_surface.blit(quit_text, (quit_button.x + 25, quit_button.y + 15))
    display_surface.blit(reset_text, (reset_button.x + 25, reset_button.y + 15))
    display_surface.blit(menu_text, (menu_button.x + 25, menu_button.y + 15))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if quit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif reset_button.collidepoint(event.pos):
                    return "reset"
                elif menu_button.collidepoint(event.pos):
                    return "menu"

class Start:
    def __init__(self, perso_color, prop_image, x_prop, y_prop):
        self.run_game(perso_color, prop_image, x_prop, y_prop)

    def run_game(self, perso_color, prop_image, x_prop, y_prop):
        from MainMenu import MainMenu
        pygame.init()

        display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption('Pygame Flappy Bird')
        clock = pygame.time.Clock()
        score_font = pygame.font.SysFont(None, 32, bold=True)
        images = load_images()

        LunettesDeSoleil = pygame.image.load("Assets/lunettes-de-soleil.jpg").convert_alpha()
        LunettesDeSoleil = pygame.transform.scale(LunettesDeSoleil, (40,40))
        LunettesDeSoleil.set_colorkey((253, 253, 253))

        
        bird = personnalisedBird(50, int(WIN_HEIGHT/2 - personnalisedBird.HEIGHT/2), 2, (images['bird-wingup'], images['bird-wingdown']),perso_color,prop_image,x_prop,y_prop)
        pipes = deque()
        frame_clock = 0
        score = 0
        done = paused = False

        while not done:
            clock.tick(FPS)

            if not (paused or frame_clock % msec_to_frames(PipePair.ADD_INTERVAL)):
                pp = PipePair(images['pipe-end'], images['pipe-body'])
                pipes.append(pp)

            for e in pygame.event.get():
                if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                    done = True
                    break
                elif e.type == KEYUP and e.key in (K_PAUSE, K_p):
                    paused = not paused
                elif e.type == MOUSEBUTTONUP or (e.type == KEYUP and e.key in (K_UP, K_RETURN, K_SPACE)):
                    #bird.msec_to_climb = Bird.CLIMB_DURATION
                    bird.msec_to_climb = personnalisedBird.CLIMB_DURATION


            if paused:
                continue

            pipe_collision = any(p.collides_with(bird) for p in pipes)

            #if pipe_collision or 0 >= bird.y or bird.y >= WIN_HEIGHT - personnalisedBird.HEIGHT:
            if pipe_collision or 0 >= bird.y or bird.y >= WIN_HEIGHT - personnalisedBird.HEIGHT:
                result = game_over_screen(display_surface, score)
                if result == "reset":
                    # Reset the game
                    #bird = Bird(50, int(WIN_HEIGHT/2 - Bird.HEIGHT/2), 2, (images['bird-wingup'], images['bird-wingdown']))
                    bird = personnalisedBird(50, int(WIN_HEIGHT/2 - personnalisedBird.HEIGHT/2), 2, (images['bird-wingup'], images['bird-wingdown']),perso_color,prop_image,x_prop,y_prop)
                    pipes.clear()
                    frame_clock = 0
                    score = 0
                    paused = False
                elif result == "menu":
                    MainMenu().run()
                    return MainMenu().run()
                #self.fenetre.blit(self.fond, (0, 0))
                    
                else:
                    done = True

            for x in (0, WIN_WIDTH / 2):
                display_surface.blit(images['background'], (x, 0))

            while pipes and not pipes[0].visible:
                pipes.popleft()

            for p in pipes:
                p.update()
                display_surface.blit(p.image, p.rect)

            bird.update()
            display_surface.blit(bird.image, bird.rect)

            for p in pipes:
                if p.x + PipePair.WIDTH < bird.x and not p.score_counted:
                    score += 1
                    p.score_counted = True

            score_surface = score_font.render(str(score), True, (255, 255, 255))
            score_x = WIN_WIDTH/2 - score_surface.get_width()/2
            display_surface.blit(score_surface, (score_x, PipePair.PIECE_HEIGHT))

            pygame.display.flip()

            frame_clock += 1

        print('Game over! Score: %i' % score)
        pygame.quit()

if __name__ == '__main__':
    Start()
