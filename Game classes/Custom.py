
import pygame
from pygame.locals import *
from PIL import Image
import os

from MenuManager import MenuManager

class Custom(MenuManageur) :
def display_custom():
    pygame.init()

    SCREEN_WIDTH_CUSTOM = 600
    SCREEN_HEIGHT_CUSTOM = 600
    fenetre = pygame.display.set_mode((SCREEN_WIDTH_CUSTOM, SCREEN_HEIGHT_CUSTOM))

    fond = pygame.image.load('Assets/background2.jpg')
    fenetre.blit(fond, (0, 0))



    # Chargement des personnages
    persoRouge = pygame.image.load("Assets/FlappyBird0.png").convert_alpha()
    nouvelle_taille = (90, 90)
    persoRouge = pygame.transform.scale(persoRouge, nouvelle_taille)
    position_persoRouge = persoRouge.get_rect()
    position_persoRouge.topleft = (100, 300)

    persoJaune = pygame.image.load("Assets/bird1.png").convert_alpha()
    persoJaune = pygame.transform.scale(persoJaune, nouvelle_taille)
    persoJaune.set_colorkey((255, 255, 255))



    persoBleu = pygame.image.load("Assets/OiseauBleu.png").convert_alpha()
    persoBleu = pygame.transform.scale(persoBleu, nouvelle_taille)
    persoBleu.set_colorkey((255, 255, 255))





    # Chargement des accessoires
    chapeauCowboy = pygame.image.load("Assets/chapeau_cowboy.png").convert_alpha()
    chapeauCowboy = pygame.transform.scale(chapeauCowboy, nouvelle_taille)

    LunettesDeSoleil = pygame.image.load("Assets/lunettes-de-soleil.jpg").convert_alpha()
    LunettesDeSoleil = pygame.transform.scale(LunettesDeSoleil, nouvelle_taille)
    LunettesDeSoleil.set_colorkey((253, 253, 253))

    tuba = pygame.image.load("Assets/tuba.jpg").convert_alpha()
    tuba = pygame.transform.scale(tuba, nouvelle_taille)
    tuba.set_colorkey((255, 255, 255))



    #Différentes combinaisons
    RougeLunettes= pygame.image.load("Assets/RougeLunettes.png").convert_alpha()
    RougeLunettes= pygame.transform.scale(RougeLunettes, nouvelle_taille)

    RougeChapeau= pygame.image.load("Assets/RougeChapeau.png").convert_alpha()
    RougeChapeau= pygame.transform.scale(RougeChapeau, nouvelle_taille)

    RougeTuba= pygame.image.load("Assets/RougeTuba.png").convert_alpha()
    RougeTuba= pygame.transform.scale(RougeTuba, nouvelle_taille)

    BleuLunettes= pygame.image.load("Assets/BleuLunettes.png").convert_alpha()
    BleuLunettes= pygame.transform.scale(BleuLunettes, nouvelle_taille)

    BleuChapeau= pygame.image.load("Assets/BleuChapeau.png").convert_alpha()
    BleuChapeau= pygame.transform.scale(BleuChapeau, nouvelle_taille)

    BleuTuba= pygame.image.load("Assets/BleuTuba.png").convert_alpha()
    BleuTuba= pygame.transform.scale(BleuTuba, nouvelle_taille)

    JauneLunettes= pygame.image.load("Assets/JauneLunettes.png").convert_alpha()
    JauneLunettes= pygame.transform.scale(JauneLunettes, nouvelle_taille)

    JauneChapeau= pygame.image.load("Assets/JauneChapeau.png").convert_alpha()
    JauneChapeau= pygame.transform.scale(JauneChapeau, nouvelle_taille)

    JauneTuba= pygame.image.load("Assets/JauneTuba.png").convert_alpha()
    JauneTuba= pygame.transform.scale(JauneTuba, nouvelle_taille)


    # Définition du bouton bleu
    BUTTON_WIDTH = 50
    BUTTON_HEIGHT = 50
    bouton_Bleu_Rect = pygame.Rect((SCREEN_WIDTH_CUSTOM - BUTTON_WIDTH) // 2, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
    # Surface pour le fond bleu du bouton
    bouton_Bleu_Fond = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
    bouton_Bleu_Fond.fill((0, 0, 255))
    # Surface pour les bordures noires du bouton
    bouton_Bleu_Bordures = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(bouton_Bleu_Bordures, (0, 0, 0), bouton_Bleu_Bordures.get_rect(), 2)
    # Combinaison du fond et des bordures
    bouton_Bleu_Text = bouton_Bleu_Fond.copy()
    bouton_Bleu_Text.blit(bouton_Bleu_Bordures, (0, 0))


    # Définition du bouton rouge
    bouton_Rouge_Rect = pygame.Rect(SCREEN_WIDTH_CUSTOM - BUTTON_WIDTH - 150, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
    # Surface pour le fond rouge du bouton
    bouton_Rouge_Fond = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
    bouton_Rouge_Fond.fill((255, 0, 0))
    # Surface pour les bordures noires du bouton
    bouton_Rouge_Bordures = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(bouton_Rouge_Bordures, (0, 0, 0), bouton_Rouge_Bordures.get_rect(), 2)
    # Combinaison du fond et des bordures
    bouton_Rouge_Text = bouton_Rouge_Fond.copy()
    bouton_Rouge_Text.blit(bouton_Rouge_Bordures, (0, 0))


    # Définition du bouton Jaune
    bouton_Jaune_Rect = pygame.Rect(150, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
    # Surface pour le fond Jaune du bouton
    bouton_Jaune_Fond = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
    bouton_Jaune_Fond.fill((255, 255, 0))
    # Surface pour les bordures noires du bouton
    bouton_Jaune_Bordures = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT), pygame.SRCALPHA)
    pygame.draw.rect(bouton_Jaune_Bordures, (0, 0, 0), bouton_Jaune_Bordures.get_rect(), 2)
    # Combinaison du fond et des bordures
    bouton_Jaune_Text = bouton_Jaune_Fond.copy()
    bouton_Jaune_Text.blit(bouton_Jaune_Bordures, (0, 0))




    # Position initiale du chapeauCowboy
    position_chapeauCowboy = chapeauCowboy.get_rect()
    position_chapeauCowboy.topleft = (400, 200)

    # Position initiale des lunettes de soleil
    position_LunettesDeSoleil = LunettesDeSoleil.get_rect()
    position_LunettesDeSoleil.topleft = (400, 100)

    # Position initiale du tuba
    position_tuba = tuba.get_rect()
    position_tuba.topleft = (400, 300)

    # Variables pour le suivi de l'état de déplacement de chaque accessoire
    en_deplacement_chapeauCowboy = False
    en_deplacement_LunettesDeSoleil = False
    en_deplacement_tuba = False
    en_deplacement_perso = False  





    perso=persoRouge
    position_perso=position_persoRouge


    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                 running = False
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if bouton_Bleu_Rect.collidepoint(event.pos):
                        perso = persoBleu
                        position_perso = position_persoRouge
                    elif bouton_Rouge_Rect.collidepoint(event.pos):
                        perso = persoRouge
                        position_perso = position_persoRouge
                    elif bouton_Jaune_Rect.collidepoint(event.pos):
                        perso = persoJaune
                        position_perso = position_persoRouge
                    elif position_chapeauCowboy.collidepoint(event.pos):
                        en_deplacement_chapeauCowboy = True
                        offset_x, offset_y = position_chapeauCowboy.topleft[0] - event.pos[0], position_chapeauCowboy.topleft[1] - event.pos[1]
                    elif position_LunettesDeSoleil.collidepoint(event.pos):
                        en_deplacement_LunettesDeSoleil = True
                        offset_x, offset_y = position_LunettesDeSoleil.topleft[0] - event.pos[0], position_LunettesDeSoleil.topleft[1] - event.pos[1]
                    elif position_tuba.collidepoint(event.pos):
                        en_deplacement_tuba = True
                        offset_x, offset_y = position_tuba.topleft[0] - event.pos[0], position_tuba.topleft[1] - event.pos[1]
                    elif position_perso.collidepoint(event.pos):
                        en_deplacement_perso = True
                        offset_x, offset_y = position_perso.topleft[0] - event.pos[0], position_perso.topleft[1] - event.pos[1]
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    en_deplacement_chapeauCowboy = False
                    en_deplacement_LunettesDeSoleil = False
                    en_deplacement_tuba = False
                    en_deplacement_perso = False
                    if en_deplacement_chapeauCowboy:
                        if perso == persoJaune:
                            perso = JauneChapeau
                        elif perso == persoBleu:
                            perso = BleuChapeau
                        elif perso == persoRouge:
                            perso = RougeChapeau
                    elif en_deplacement_LunettesDeSoleil:
                        if perso == persoJaune:
                            perso = JauneLunettes
                        elif perso == persoBleu:
                            perso = BleuLunettes
                        elif perso == persoRouge:
                            perso = RougeLunettes
                    elif en_deplacement_tuba:
                        if perso == persoJaune:
                            perso = JauneTuba
                        elif perso == persoBleu:
                            perso = BleuTuba
                        elif perso == persoRouge:
                            perso = RougeTuba

            elif event.type == MOUSEMOTION:
                if en_deplacement_chapeauCowboy:
                    position_chapeauCowboy.topleft = (event.pos[0] + offset_x, event.pos[1] + offset_y)
                elif en_deplacement_LunettesDeSoleil:
                    position_LunettesDeSoleil.topleft = (event.pos[0] + offset_x, event.pos[1] + offset_y)
                elif en_deplacement_tuba:
                    position_tuba.topleft = (event.pos[0] + offset_x, event.pos[1] + offset_y)
                elif en_deplacement_perso:
                    position_perso.topleft = (event.pos[0] + offset_x, event.pos[1] + offset_y)


    
    
    
    
    
    
        # Effacer l'écran
        fenetre.fill((0, 0, 0))

        # Redessiner le fond
        fenetre.blit(fond, (0, 0))

        # Afficher le bouton bleu
        pygame.draw.rect(fenetre, (255, 255, 255), bouton_Bleu_Rect)
        text_x = bouton_Bleu_Rect.x + (bouton_Bleu_Rect.width - bouton_Bleu_Text.get_width()) // 2
        text_y = bouton_Bleu_Rect.y + (bouton_Bleu_Rect.height - bouton_Bleu_Text.get_height()) // 2
        fenetre.blit(bouton_Bleu_Text, (text_x, text_y))

        # Afficher le bouton Rouge
        pygame.draw.rect(fenetre, (255, 255, 255), bouton_Rouge_Rect)
        text_x = bouton_Rouge_Rect.x + (bouton_Rouge_Rect.width - bouton_Rouge_Text.get_width()) // 2
        text_y = bouton_Rouge_Rect.y + (bouton_Rouge_Rect.height - bouton_Rouge_Text.get_height()) // 2
        fenetre.blit(bouton_Rouge_Text, (text_x, text_y))

        # Afficher le bouton Jaune
        pygame.draw.rect(fenetre, (255, 255, 255), bouton_Jaune_Rect)
        text_x = bouton_Jaune_Rect.x + (bouton_Jaune_Rect.width - bouton_Jaune_Text.get_width()) // 2
        text_y = bouton_Jaune_Rect.y + (bouton_Jaune_Rect.height - bouton_Jaune_Text.get_height()) // 2
        fenetre.blit(bouton_Jaune_Text, (text_x, text_y))
    
    
        # Redessiner le personnage
        fenetre.blit(perso, position_perso)

        # Redessiner les accessoires
        fenetre.blit(chapeauCowboy, position_chapeauCowboy)
        fenetre.blit(LunettesDeSoleil, position_LunettesDeSoleil)
        fenetre.blit(tuba, position_tuba)

        pygame.display.flip()

    pygame.quit()

display_custom()
