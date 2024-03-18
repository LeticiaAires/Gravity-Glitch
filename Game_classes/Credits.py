import os
import pygame
import sys
import random
rnd = random.Random()

from MenuManager import MenuManager  # Importation de la classe parente MenuManager depuis le fichier MenuManager.py




#class for the credits
class CreditsMenu(MenuManager): 
    def __init__(self):
        super().__init__()
        # Paramètres d'affichage
        self.fenetre = pygame.display.set_mode((MenuManager.SCREEN_WIDTH, MenuManager.SCREEN_HEIGHT))
        pygame.display.set_caption("Crédits")

        # Chargement de l'image de fond
        self.fond = pygame.image.load('Assets/background2.jpg')
        # Liste de crédits
        self.credits = [
            "Developers : Mantoulaye MBENGUE, Solene CERPAC, Leticia AIRES, ​",
            "                       Cassandre CHANDELIER, Zineb LAHMOUDI",
            "",
            "",
            "Menu : Mantoulaye MBENGUE",
            "",
            "Coordination transverse : Mantoulaye MBENGUE",
            "",
            "History Mode : Leticia AIRES and Cassandre CHANDELIER",
            "",
            "Design background : Leticia AIRES",
            "",
            "Runner : Leticia AIRES",
            "",
            "Random Obstacles : Solene CERPAC et Zineb LAHMOUDI",
            "",
            "Credits : Solene CERPAC",
            "",
            "Rules : Zineb LAHMOUDI",
            "",
            "Game Tester : Nicolas Papazoglou",
            "",
            "Game Tester : Laurent Fiack",
            "",
            "Song : Clement Panchout 'Life is full of Joy'"
        ]

        self.bouton_retour = pygame.Rect(600, 300, 200, 50)
        self.font_filename = "your_font.ttf"
        self.font_path = os.path.join("Assets", MenuManager.font_filename)
        self.button_font = pygame.font.Font(MenuManager.font_path, 20)

        self.y_position = MenuManager.SCREEN_HEIGHT
        self.return_font = pygame.font.Font(MenuManager.font_path, 30)
        self.bouton_retour = self.return_font.render("Return", True, (0,0,0))
        self.return_rect = pygame.Rect((MenuManager.SCREEN_WIDTH - MenuManager.BUTTON_WIDTH) // 1, 500, MenuManager.BUTTON_WIDTH, MenuManager.BUTTON_HEIGHT)
        self.defilement_actif = True
    def run(self):
            bouton_retour = self.bouton_retour
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        print("Mouse pos : "+ str(mouse_pos))
                        print(str(bouton_retour))
                        print(str(self.return_rect.collidepoint(mouse_pos)))
                        if self.return_rect.collidepoint(mouse_pos):
                            # L'utilisateur a cliqué sur le bouton "Retour"
                            running = False
                            return "main"
                self.fenetre.blit(self.fond, (0, 0))
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.bouton_retour, mouse_pos1)
                if self.defilement_actif:
                    for i, ligne in enumerate(self.credits):
                        texte = self.button_font.render(ligne, True, (0, 0, 0))
                        y = self.y_position + i * 40
                        self.fenetre.blit(texte, (40, y))

                    self.y_position -= 0.2

                    if self.y_position < -len(self.credits) * 45:
                        defilement_actif = False

                self.fenetre.blit(self.bouton_retour, (self.return_rect.centerx - self.bouton_retour.get_width() // 2, self.return_rect.centery - self.bouton_retour.get_height() // 2))
                pygame.display.update()
                pygame.display.flip() 
#Function to increase the size of a button when the mouse is on it 
    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = MenuManager.BUTTON_WIDTH + 20
            button_rect.h = MenuManager.BUTTON_HEIGHT + 10
        else:
            button_rect.w = MenuManager.BUTTON_WIDTH
            button_rect.h = MenuManager.BUTTON_HEIGHT  

