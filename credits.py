import pygame
import sys
from menu import display_menu
import os
import pygame.mixer


def display_credits():
    # Initialisation de Pygame
    pygame.init()

    # Paramètres d'affichage
    SCREEN_WIDTH_CREDITS, SCREEN_HEIGHT_CREDITS = 1550, 800
    BUTTON_WIDTH = 180
    BUTTON_HEIGHT = 60
    fenetre = pygame.display.set_mode((SCREEN_WIDTH_CREDITS, SCREEN_HEIGHT_CREDITS))
    pygame.display.set_caption("Crédits")

    # Chargement de l'image de fond
    fond = pygame.image.load('Assets/background2.jpg')

    # Redimensionnez l'image de fond pour correspondre à la taille de l'écran
    fond = pygame.transform.scale(fond, (SCREEN_WIDTH_CREDITS, SCREEN_HEIGHT_CREDITS))

    # Liste de crédits
    credits = [
        "Développeuses : Mantoulaye MBENGUE, Solène CERPAC, Letícia AIRES, ​",
        "                       Cassandre CHANDELIER, Zineb LAHMOUDI",
        "",
        "",
        "Menu : Mantoulaye MBENGUE",
        "",
        "Compositeur musical : Mantoulaye MBENGUE",
        "",
        "Oiseau : Cassandre CHANDELIER",
        "",
        "Design background : Letícia AIRES",
        "",
        "Runner : Letícia AIRES",
        "",
        "Obstacles aléatoires quantiques : Solène CERPAC",
        "",
        "Obstacles aléatoires quantiques : Zineb LAHMOUDI",
        "",
        "Crédits : Solène CERPAC",
        "",
        "Testeur de jeu : Nicolas Papazoglou",
        "",
        "Testeur de jeu : Laurent Fiack",
        "",
        "Musique : Clement Panchout 'Life is full of Joy'"
    ]

    bouton_retour = pygame.Rect(600, 300, 200, 50)
    font_filename = "your_font.ttf"
    font_path = os.path.join("Assets", font_filename)
    button_font = pygame.font.Font(font_path, 36)
    BUTTON_WIDTH = 180
    BUTTON_HEIGHT = 60

    y_position = SCREEN_HEIGHT_CREDITS
    defilement_actif = True
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print("Mouse pos : "+ str(mouse_pos))
                print(str(bouton_retour))
                print(str(bouton_retour.collidepoint(mouse_pos)))
                if bouton_retour.collidepoint(mouse_pos):
                    # L'utilisateur a cliqué sur le bouton "Menu"
                    # Vous pouvez appeler la fonction menu_display() ici
                    display_menu()

        fenetre.blit(fond, (0, 0))

        if defilement_actif:
            for i, ligne in enumerate(credits):
                texte = button_font.render(ligne, True, (0, 0, 0))
                y = y_position + i * 40
                fenetre.blit(texte, (50, y))

            y_position -= 0.5

            if y_position < -len(credits) * 45:
                defilement_actif = False

        if not defilement_actif:
            credits_button = button_font.render("Menu", True, (0, 0, 0))
            credits_rect = pygame.Rect((SCREEN_WIDTH_CREDITS - BUTTON_WIDTH) // 2, 300, BUTTON_WIDTH, BUTTON_HEIGHT)
            pygame.draw.rect(fenetre, (255, 255, 255), credits_rect)
            text_x = credits_rect.x + (credits_rect.width - credits_button.get_width()) // 2
            text_y = credits_rect.y + (credits_rect.height - credits_button.get_height()) // 2
            fenetre.blit(credits_button, (text_x, text_y))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


display_credits()
