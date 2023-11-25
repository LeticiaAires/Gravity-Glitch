import pygame
from pygame.locals import *
import random
import os


pygame.init()

clock = pygame.time.Clock() #to control the speed of the framerate
fps=40


SCREEN_WIDTH,SCREEN_HEIGHT =800,600

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Gravity Glitch')

# Define the font file and path
font_filename = "your_font.ttf"
font_path = os.path.join("Assets/your_font.ttf", font_filename)
run=True
#define game variables
scroll_speed=4
ground_scroll=0


#load images
BG=pygame.image.load("Assets/background2.jpg")
#ground_img=pygame.image.load('Assets/ground.png')

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y): #self is like "this" in Java with implicit declarations
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for num in range (1,4):  
            img=pygame.image.load(f'Assets/bird{num}.png')
            self.images.append(img)
        self.image=pygame.image.load('Assets/bird1.png')
        self.rect=self.image.get_rect() #creates a rectangle from the boundary of that image
        self.rect.center=[x,y]
def update(self):
    #handle the animation
    self.counter+=1
    flap_cooldown=5

    if self.counter<flap_cooldown:
        self.counter=0
        self.index+=1


bird_group=pygame.sprite.Group()

#creation of an instance
flappy=Bird(100,int(SCREEN_HEIGHT/2))

bird_group.add(flappy)



while run:
    clock.tick(fps)
    #draw background
    screen.blit(BG,(0,0))

    bird_group.draw(screen)
    bird_group.update(screen)
    #scroll the BG
    screen.blit(BG,(ground_scroll,0))
    ground_scroll-=scroll_speed
    if abs(ground_scroll)>35 : #if that ground_scroll exceeds the value of the pixels of our BG
        ground_scroll=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
    pygame.display.update()



pygame.quit()