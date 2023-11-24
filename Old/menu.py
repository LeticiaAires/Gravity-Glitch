import pygame
import sys
import os

# initialising pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Constants for button dimensions
BUTTON_WIDTH = 180
BUTTON_HEIGHT = 40

# function to display the menu window
def display_menu():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Menu Example")

    # Design of the menu
    background_image = pygame.image.load("background.jpg").convert()
    background_rect = background_image.get_rect()
    # Replace "your_font.ttf" with the correct font file name
    font_filename = "your_font.ttf"

    # Full path to your font file
    font_path = os.path.join("C:\Users\zinef\Downloads\GAME\2324_Projet2A_JeuVideo", font_filename)

    # Load custom font for the title
    title_font = pygame.font.Font(font_path, 50)
    title_text = title_font.render("Welcome to Gravity Glitch", True, (0, 0, 0))
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, 50))

    # Display a "Play" button
    button_font = pygame.font.Font(None, 36)
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

        # Update the display
        screen.blit(background_image, background_rect)
        screen.blit(title_text, title_rect)

        pygame.draw.rect(screen, (0, 0, 0), play_rect, 4)
        pygame.draw.rect(screen, (0, 0, 0), rules_rect, 4)
        pygame.draw.rect(screen, (0, 0, 0), credits_rect, 4)
        pygame.draw.rect(screen, (0, 0, 0), options_rect, 4)

        screen.blit(play_button, (play_rect.centerx - play_button.get_width() // 2, play_rect.centery - play_button.get_height() // 2))
        screen.blit(rules_button, (rules_rect.centerx - rules_button.get_width() // 2, rules_rect.centery - rules_button.get_height() // 2))
        screen.blit(credits_button, (credits_rect.centerx - credits_button.get_width() // 2, credits_rect.centery - credits_button.get_height() // 2))
        screen.blit(options_button, (options_rect.centerx - options_button.get_width() // 2, options_rect.centery - options_button.get_height() // 2))

        pygame.display.update()

    pygame.quit()

display_menu()
