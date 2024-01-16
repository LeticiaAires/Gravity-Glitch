import pygame
import sys
from PseudoChoice import NameMenu
from Rules import RulesMenu
from Credits import CreditsMenu
from Settings import SettingMenu
from MainMenu import MainMenu
from Game import run_game  # Import the run_game function from game.py
from PauseWindow import PauseWindow
from MenuManager import MenuManager
from Custom import Custom

# Initializing pygame
pygame.init()

# Defining the size of the game window
windowsSize = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello World Printer")

# Defining font attributes
myFont = pygame.font.SysFont("Segoe UI", 90)
helloWorld = myFont.render("You did it!!!", 1, (255, 0, 255), (255, 255, 255))

# Creating instances of each menu
main_menu = MainMenu()
settings_menu = SettingMenu()
credits_menu = CreditsMenu()
name_menu = NameMenu()
rules_menu = RulesMenu()
pause_menu = PauseWindow()
custom_menu = Custom()

running = True
current_menu = "main"
active_menu = main_menu
while running:
    # Check if the current menu is the game and run it
    if current_menu == "play":
        run_game()  # Call the function to start the game
    else:
        active_menu.run()

    # Rest of your code...

    if current_menu == "quit":
        active_menu = None
        running = False
        sys.exit()
    else:
        running = False  # Exit the game loop if needed

    # Quit Pygame
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()
