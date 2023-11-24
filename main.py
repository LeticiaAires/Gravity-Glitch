
import pygame 
import sys


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


# Run the main menu
if __name__ == "__main__":
    menu = MainMenu()
    running = True
    while running:
        # Check the current menu screen state
        current_menu = menu.run()
        # Act based on the menu the user returns from
        if current_menu == "main":
            menu = MainMenu()
        elif current_menu == "settings":
            menu = SettingMenu()
        elif current_menu == "credits":
            menu = CreditsMenu()
        elif current_menu == "play":
            menu = GameMenu()   
        elif current_menu == "rules":
            menu = RulesMenu()   
        else:
            running = False  # If the user decides to quit the game

# Quit Pygame
pygame.mixer.quit()
pygame.quit()