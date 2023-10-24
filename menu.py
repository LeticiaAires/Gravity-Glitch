import pygame
import pygame.mixer
import sys
import os
import random
# Initialize pygame
pygame.init()
pygame.mixer.init()
global music_playing
music_playing = False
global changed
changed = 0 #the music hasn't been touched

# Constants 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 60


# Define the font file and path
font_filename = "your_font.ttf"
font_path = os.path.join("Assets", font_filename)

# Function to display the menu window
def display_menu():
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Menu Gravity Glitch")

    # Load background image
    background_image = pygame.image.load("Assets/background2.jpg").convert()
    background_rect = background_image.get_rect()

    # Load custom font for the title and buttons
    title_font = pygame.font.Font(font_path, 50)
    button_font = pygame.font.Font(font_path, 36)
    #load the music file if the settings haven't been changed
    if changed == 0 and music_playing==False: 
        pygame.mixer.music.load('Assets/music_menu.wav')
        pygame.mixer.music.play(-1)
    elif changed ==1 :
        pygame.mixer.music.stop()
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
    setting_button = button_font.render("Settings", True, (0, 0, 0))
    setting_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 400, BUTTON_WIDTH, BUTTON_HEIGHT)

        #Display a "Quit" button
    quit_button = button_font.render("Quit", True, (0, 0, 0))
    quit_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
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
                    #credits à ajouter : 2016_ Clement Panchout_ Life is full of Joy
                elif setting_rect.collidepoint(mouse_pos):
                    print("The button 'Settings' has been pressed")
                    display_setting()
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

            if setting_rect.collidepoint(mouse_pos):
                setting_rect.w = BUTTON_WIDTH + 20
                setting_rect.h = BUTTON_HEIGHT + 10
            else:
                setting_rect.w = BUTTON_WIDTH
                setting_rect.h = BUTTON_HEIGHT

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
        screen.blit(setting_button, (setting_rect.centerx - setting_button.get_width() // 2, setting_rect.centery - setting_button.get_height() // 2))
        screen.blit(quit_button, (quit_rect.centerx - quit_button.get_width() // 2, quit_rect.centery - quit_button.get_height() // 2))

        pygame.display.update()
    pygame.mixer.quit()
    pygame.quit()

# Function to display the setting
def display_setting():
    global music_playing
    global changed
    pygame.init()  # Initialize the video system
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running1 = True

    # Design of the settings
    background_setting_image = pygame.image.load("Assets/background2.jpg").convert()
    background_setting_rect = background_setting_image.get_rect()
    font_filename = "your_font.ttf"
        # Full path to your font file
    font_path = os.path.join("Assets", font_filename)
        # Load custom font for the title of the Settings
    title_setting_font = pygame.font.Font(font_path, 50)
    title_setting_text = title_setting_font.render(" Settings ", True, (255,255,255))
    title_setting_rect = title_setting_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

        # Display a "Return" button
    return_font = pygame.font.Font(font_path, 30) 
    return_button = return_font.render("Return", True, (0, 0, 0))
    return_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 6, 500, BUTTON_WIDTH, BUTTON_HEIGHT)
    # Create text surfaces
    setting_font = pygame.font.Font(font_path, 40)
    musicon_text = setting_font.render(" Music ON ", True, (0, 0, 0))
    musicoff_text = setting_font.render(" Music OFF ", True, (0, 0, 0))
    # Set positions for the text
    musicon_rect = musicon_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
    musicoff_rect = musicoff_text.get_rect(center=(SCREEN_WIDTH // 2, 300))
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
                elif musicoff_rect.collidepoint(mouse_pos):
                    print("The button 'music off' has been pressed")
                    pygame.mixer.music.stop()
                    music_playing = False  # Update the variable when music is stopped
                    changed = 1
                elif musicon_rect.collidepoint(mouse_pos):
                    print("The button 'music on' has been pressed")
                    pygame.mixer.music.load('Assets/music_menu.wav')
                    pygame.mixer.music.play(-1)
                    music_playing = True  # Update the variable when music is playing
                    changed = 0 #we clicked on on
        mouse_pos1 = pygame.mouse.get_pos()
         # Check if the mouse is over a button and increase its size accordingly
        if return_rect.collidepoint(mouse_pos1):
            return_rect.w = BUTTON_WIDTH + 20
            return_rect.h = BUTTON_HEIGHT + 10
        else:
            return_rect.w = BUTTON_WIDTH
            return_rect.h = BUTTON_HEIGHT

        if musicon_rect.collidepoint(mouse_pos1):
            musicon_rect.w = BUTTON_WIDTH + 20
            musicon_rect.h = BUTTON_HEIGHT + 10
        else:
            musicon_rect.w = BUTTON_WIDTH
            musicon_rect.h = BUTTON_HEIGHT
        if musicoff_rect.collidepoint(mouse_pos1):
            musicoff_rect.w = BUTTON_WIDTH + 20
            musicoff_rect.h = BUTTON_HEIGHT + 10
        else:
            musicoff_rect.w = BUTTON_WIDTH
            musicoff_rect.h = BUTTON_HEIGHT
            # Update the display
        screen.blit(background_setting_image, (0, 0))
        screen.blit(title_setting_font.render(" Settings ", True, (0, 0, 0)), (SCREEN_WIDTH // 3 - 200, 30))
        screen.blit(return_button, (return_rect.centerx - return_button.get_width() // 2, return_rect.centery - return_button.get_height() // 2))
        screen.blit(musicon_text, (musicon_rect.centerx - musicon_text.get_width() // 2, musicon_rect.centery - musicon_text.get_height() // 2))
        screen.blit(musicoff_text, (musicoff_rect.centerx - musicoff_text.get_width() // 2, musicoff_rect.centery - musicoff_text.get_height() // 2))
        pygame.display.update()

   



# Run the menu display
if __name__ == "__main__":
    display_menu()










