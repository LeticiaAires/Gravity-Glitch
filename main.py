
import pygame 
import sys
from NameMenu import NameMenu
from RulesMenu import RulesMenu
from NewCredits import CreditsMenu
from settings import SettingMenu
from MainMenu import MainMenu
from Game import Game
from PauseWindow import PauseWindow

#initialising pygame
pygame.init()

#defining size of game window
windowsSize = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Hello World Printer")

#defining font attributes
myFont = pygame.font.SysFont("Segoe UI", 90)
helloWorld = myFont.render("You did it!!!", 1, (255, 0, 255), (255, 255, 255))

#while 1:
    #for event in pygame.event.get():
        #if event.type==pygame.QUIT: sys.exit()
    #windowsSize.blit(helloWorld, (0, 0))
    #pygame.display.update()

# Creating instances of each menu
main_menu = MainMenu()
settings_menu = SettingMenu()
credits_menu = CreditsMenu()
name_menu = NameMenu()
rules_menu = RulesMenu()
game_instance = Game()
pause_menu = PauseWindow()

# Set the initial active menu
active_menu = main_menu

# Set up the game loop
running = True
while running:
    current_menu = active_menu.run()
    if current_menu == "main":
        active_menu = main_menu
    elif current_menu == "settings":
        active_menu = settings_menu
    elif current_menu == "credits":
        active_menu = credits_menu
    elif current_menu == "play":
        active_menu = name_menu
        print("Yay it works")
    elif current_menu == "rules":
        active_menu = rules_menu
    elif current_menu == "pause":
        active_menu = pause_menu
        print("Yay it works x 2")
    else:
        running = False  # Exit the game loop if neede
# Quit Pygame
pygame.mixer.quit()
pygame.quit()