import pygame
import sys
from oldmenu import display_menu

# Initialisation de Pygame
pygame.init()

# Paramètres d'affichage
largeur, hauteur = 1400, 800
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Crédits")

# Chargement de l'image de fond
fond = pygame.image.load(r'Assets/background2.jpg')  

# Redimensionnez l'image de fond pour correspondre à la taille de l'écran
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Police de texte
police = pygame.font.Font(None, 36)

# Liste de crédits

credits = [
    "                       Développeuses : Mantoulaye MBENGUE, Solène CERPAC, Letícia AIRES, ​",
    "                                       Cassandre CHANDELIER, Zineb LAHMOUDI",
    "",
    "",
    "                           Menu : Mantoulaye MBENGUE",
    "                           Compositeur musical : Mantoulaye MBENGUE",
    "                           Oiseau : Cassandre CHANDELIER ",
    "                           Design background : Letícia AIRES ",
    "                           Runner : Letícia AIRES",
    "                           Obstacles aléatoires quantiques : Solène CERPAC",
    "                           Obstacles aléatoires quantiques : Zineb LAHMOUDI",
    "                           History game : Solène CERPAC",
    "                           Testeur de jeu : Nicolas Papazoglou",
]

# Position de départ des crédits
y_position = hauteur

# Vitesse de défilement
vitesse_defilement = 1

# Création du bouton "Retour au menu"
bouton_retour = pygame.Rect(50, 50, 200, 50)
couleur_bouton = (0, 128, 255)
texte_bouton = police.render("Retour au menu", True, (255, 255, 255))

clock = pygame.time.Clock()

def afficher_credits():
    fenetre.blit(fond, (0, 0))

    y = y_position
    for credit in credits:
        texte = police.render(credit, True, (0, 0, 0))
        fenetre.blit(texte, (50, y))
        y += 40  # Ajustez l'espacement vertical

def reset_position():
    global y_position
    y_position = hauteur


display_menu()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if bouton_retour.collidepoint(event.pos):
                display_menu()

    afficher_credits()
    fenetre.fill(couleur_bouton, bouton_retour)
    fenetre.blit(texte_bouton, (bouton_retour.x + 10, bouton_retour.y + 10))

    y_position -= vitesse_defilement  # Faites déplacer les crédits vers le haut
    pygame.display.update()
    clock.tick(60)

    # Réinitialisez la position pour une répétition
    if y_position < -len(credits) * 40:
        reset_position()