import pygame
import pygame.mixer
import sys
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()


# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Constants for button dimensions
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 60

# Define the font file and path
font_filename = "your_font.ttf"
font_path = os.path.join("C:\\Users\\mbeng\\Documents\\ENSEA_Mantou\\Python_Game_2A\\2324_Projet2A_JeuVideo", font_filename)

# Function to display the menu window
def display_menu():
    pygame.init()
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Menu Example")

    # Load background image
    background_image = pygame.image.load("background2.jpg").convert()
    background_rect = background_image.get_rect()

    # Load custom font for the title and buttons
    title_font = pygame.font.Font(font_path, 50)
    button_font = pygame.font.Font(font_path, 36)
        # Display a "Play" button
    button_font = pygame.font.Font(font_path, 36) #The font for all the buttons + size
    play_button = button_font.render("Play", True, (0, 0, 0))
    play_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 100, BUTTON_WIDTH, BUTTON_HEIGHT)

        # Display a "Rules" button
    rules_button = button_font.render("Rules", True, (0, 0, 0))
    rules_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 200, BUTTON_WIDTH, BUTTON_HEIGHT)

        # Display a "Credits" button
    credits_button = button_font.render("Credits", True, (0, 0, 0))
    credits_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)

        # Display an "Options" button
    options_button = button_font.render("Options", True, (0, 0, 0))
    options_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT)

        #Display a "Quit" button
    quit_button = button_font.render("Quit", True, (0, 0, 0))
    quit_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
    #load the music file
    pygame.mixer.music.load('jazz6.wav') 
    #play it in a loop
    pygame.mixer.music.play(-1)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_rect.collidepoint(mouse_pos):
                    print("The button 'Play' has been pressed")
                elif rules_rect.collidepoint(mouse_pos):
                    print("The button 'Rules' has been pressed")
                elif credits_rect.collidepoint(mouse_pos):
                    print("The button 'Credits' has been pressed")
                elif options_rect.collidepoint(mouse_pos):
                    print("The button 'Options' has been pressed")
                    display_options()
                elif quit_rect.collidepoint(mouse_pos):
                    print("The button 'Quit' has been pressed")
                    running=False
                    print(" Goodbye ! ")
            mouse_pos = pygame.mouse.get_pos()
            # Check if the mouse is over a button and increase its size accordingly
            if play_rect.collidepoint(mouse_pos):
                play_rect.w = BUTTON_WIDTH + 20
                play_rect.h = BUTTON_HEIGHT + 10
            else:
                play_rect.w = BUTTON_WIDTH
                play_rect.h = BUTTON_HEIGHT

            if rules_rect.collidepoint(mouse_pos):
                rules_rect.w = BUTTON_WIDTH + 20
                rules_rect.h = BUTTON_HEIGHT + 10
            else:
                rules_rect.w = BUTTON_WIDTH
                rules_rect.h = BUTTON_HEIGHT

            if credits_rect.collidepoint(mouse_pos):
                credits_rect.w = BUTTON_WIDTH + 20
                credits_rect.h = BUTTON_HEIGHT + 10
            else:
                credits_rect.w = BUTTON_WIDTH
                credits_rect.h = BUTTON_HEIGHT

            if options_rect.collidepoint(mouse_pos):
                options_rect.w = BUTTON_WIDTH + 20
                options_rect.h = BUTTON_HEIGHT + 10
            else:
                options_rect.w = BUTTON_WIDTH
                options_rect.h = BUTTON_HEIGHT

            if quit_rect.collidepoint(mouse_pos):
                quit_rect.w = BUTTON_WIDTH + 20
                quit_rect.h = BUTTON_HEIGHT + 10
            else:
                quit_rect.w = BUTTON_WIDTH
                quit_rect.h = BUTTON_HEIGHT
        # Update the display
        screen.blit(background_image, (0, 0))
        screen.blit(title_font.render("Welcome to Gravity Glitch", True, (0, 0, 0)), (SCREEN_WIDTH // 3 - 200, 30))
        screen.blit(play_button, (play_rect.centerx - play_button.get_width() // 2, play_rect.centery - play_button.get_height() // 2))
        screen.blit(rules_button, (rules_rect.centerx - rules_button.get_width() // 2, rules_rect.centery - rules_button.get_height() // 2))
        screen.blit(credits_button, (credits_rect.centerx - credits_button.get_width() // 2, credits_rect.centery - credits_button.get_height() // 2))            
        screen.blit(options_button, (options_rect.centerx - options_button.get_width() // 2, options_rect.centery - options_button.get_height() // 2))
        screen.blit(quit_button, (quit_rect.centerx - quit_button.get_width() // 2, quit_rect.centery - quit_button.get_height() // 2))

        pygame.display.update()

    pygame.quit()

# Function to display the options
def display_options():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running1 = True
    #Change of music
    #load the new music file
    pygame.mixer.music.load('rock1.wav') 
    #play it in a loop
    pygame.mixer.music.play(-1)
    # Design of the options
    background_option_image = pygame.image.load("background2.jpg").convert()
    background_option_rect = background_option_image.get_rect()
        # Replace "your_font.ttf" with the correct font file name
    font_filename = "your_font.ttf"
        # Full path to your font file
    font_path = os.path.join("C:\\Users\\mbeng\\Documents\\ENSEA_Mantou\\Python_Game_2A\\2324_Projet2A_JeuVideo", font_filename)
        # Load custom font for the title of the Options
    title_option_font = pygame.font.Font(font_path, 50)
    title_option_text = title_option_font.render(" Options ", True, (255,255,255))
    title_option_rect = title_option_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

        # Display a "Return" button
    return_font = pygame.font.Font(font_path, 30) 
    return_button = return_font.render("Return", True, (0, 0, 0))
    return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 6, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
    while running1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos() #Get the mouse position, if the mouse clicks on one of the button, a message is sent
                if return_rect.collidepoint(mouse_pos):
                    print("The button 'Return' has been pressed")
                    running1=False
                    display_menu()
        mouse_pos1 = pygame.mouse.get_pos()
         # Check if the mouse is over a button and increase its size accordingly
        if return_rect.collidepoint(mouse_pos1):
            return_rect.w = BUTTON_WIDTH + 20
            return_rect.h = BUTTON_HEIGHT + 10
        else:
            return_rect.w = BUTTON_WIDTH
            return_rect.h = BUTTON_HEIGHT
            # Update the display
        screen.blit(background_option_image, (0, 0))
        screen.blit(title_option_font.render(" Options ", True, (0, 0, 0)), (SCREEN_WIDTH // 3 - 200, 30))
        screen.blit(return_button, (return_rect.centerx - return_button.get_width() // 2, return_rect.centery - return_button.get_height() // 2))
        pygame.display.update()
    pygame.quit()

# Function to display the RULES - Zineb


# Function to display the CREDITS - Solene


# Function to display the Game - Cassandre

# Music 





# Run the menu display
display_menu()










