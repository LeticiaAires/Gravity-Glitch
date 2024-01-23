import pygame 
import sys
from PseudoChoice import NameMenu
from Rules import RulesMenu
from Credits import CreditsMenu
from Settings import SettingMenu
from MainMenu import MainMenu
from MenuManager import MenuManager
from PauseWindow import PauseWindow
from Custom import CustomMenu

# initializing pygame
pygame.init()

# defining size of the game window
windowsSize = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Hello World Printer")

# defining font attributes
myFont = pygame.font.SysFont("Segoe UI", 90)
helloWorld = myFont.render("You did it!!!", 1, (255, 0, 255), (255, 255, 255))

# Creating instances of each menu
main_menu = MainMenu()
settings_menu = SettingMenu()
credits_menu = CreditsMenu()
name_menu = NameMenu()
rules_menu = RulesMenu()
pause_menu = PauseWindow()
custom_menu = CustomMenu()

running = True
current_menu = "main"
active_menu = main_menu
while running:
    # Check if the current menu is the game and run it
    if current_menu == "play":
        run_game()  # Call the main function of the Game class
    else:
        active_menu.run()



    if current_menu == "quit":
        active_menu = None
        running = False
        sys.exit()
    else:
        running = False  # Exit the game loop if neede