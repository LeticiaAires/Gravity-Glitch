
import pygame
from pygame.locals import *
#from PIL import Image
import os

from MenuManager import MenuManager
from Game import Start
from PersonnalizedBird import personnalisedBird

class CustomMenu(MenuManager) :
    def __init__(self):
        pygame.init()

        SCREEN_WIDTH_CUSTOM = 600
        SCREEN_HEIGHT_CUSTOM = 600
        self.fenetre = pygame.display.set_mode((SCREEN_WIDTH_CUSTOM, SCREEN_HEIGHT_CUSTOM))

        self.fond = pygame.image.load('Assets/background2.jpg')
        self.fenetre.blit(self.fond, (0, 0))

        self.button_font = pygame.font.Font(self.font_path, 36)
        self.play_button = self.button_font.render("Play", True, self.class_BLACK)
        self.play_rect = pygame.Rect((self.SCREEN_WIDTH - self.BUTTON_WIDTH) // 2, 500, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        

       

        # Chargement des personnages
        image = pygame.image.load("Game_classes/images/bird_wing_down.png").convert_alpha()
        nouvelle_taille = (90,90)
        image = pygame.transform.scale(image, nouvelle_taille)

        self.perso = personnalisedBird(100, 300, 0, (image,image),pygame.color.Color('white'),None,None,None)
        #self.persoJaune = personnalisedBird(1000, 1000, 0, (image,image),pygame.color.Color('white'),None,None,None)
        #self.persoBleu = personnalisedBird(1000, 1000, 0, (image,image),pygame.color.Color('blue'),None,None,None)

        #persoRouge = pygame.image.load("images/bird_wing_down.png").convert_alpha()
        #nouvelle_taille = (90, 90)
        #persoRouge = pygame.transform.scale(persoRouge, nouvelle_taille)
        #position_persoRouge = persoRouge.get_rect()
        #position_persoRouge.topleft = (100, 300)
    
        #persoJaune = pygame.image.load("Assets/bird1.png").convert_alpha()
        #persoJaune = pygame.transform.scale(persoJaune, nouvelle_taille)
        #persoJaune.set_colorkey((255, 255, 255))



        #persoBleu = pygame.image.load("Assets/OiseauBleu.xcf").convert_alpha()
        #persoBleu = pygame.transform.scale(persoBleu, nouvelle_taille)
        # Définir les couleurs à rendre transparentes
        #persoBleu.set_colorkey((255, 255, 255))
        

        # Chargement des accessoires
        self.chapeauCowboy = pygame.image.load("Assets/chapeau_cowboy.png").convert_alpha()
        self.chapeauCowboy = pygame.transform.scale(self.chapeauCowboy, nouvelle_taille)
    
        self.LunettesDeSoleil = pygame.image.load("Assets/lunettes-de-soleil.jpg").convert_alpha()
        self.LunettesDeSoleil = pygame.transform.scale(self.LunettesDeSoleil, nouvelle_taille)
        self.LunettesDeSoleil.set_colorkey((253, 253, 253))
    
        self.tuba = pygame.image.load("Assets/tuba.jpg").convert_alpha()
        self.tuba = pygame.transform.scale(self.tuba, nouvelle_taille)
        self.tuba.set_colorkey((255, 255, 255))

        
        # Définition du bouton bleu
        BUTTON_WIDTH = 50
        BUTTON_HEIGHT = 50
        self.bouton_Bleu_Rect = pygame.Rect((SCREEN_WIDTH_CUSTOM - BUTTON_WIDTH) // 2, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
        # Surface pour le fond bleu du bouton
        self.bouton_Bleu_Fond = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.bouton_Bleu_Fond.fill((0, 0, 255))
        # Surface pour les bordures noires du bouton
        self.bouton_Bleu_Bordures = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.bouton_Bleu_Bordures, (0, 0, 0), self.bouton_Bleu_Bordures.get_rect(), 2)
        # Combinaison du fond et des bordures
        self.bouton_Bleu_Text = self.bouton_Bleu_Fond.copy()
        self.bouton_Bleu_Text.blit(self.bouton_Bleu_Bordures, (0, 0))
    

        # Définition du bouton rouge
        self.bouton_Rouge_Rect = pygame.Rect(SCREEN_WIDTH_CUSTOM - BUTTON_WIDTH - 150, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
        # Surface pour le fond rouge du bouton
        self.bouton_Rouge_Fond = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.bouton_Rouge_Fond.fill((255, 0, 0))
        # Surface pour les bordures noires du bouton
        self.bouton_Rouge_Bordures = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.bouton_Rouge_Bordures, (0, 0, 0), self.bouton_Rouge_Bordures.get_rect(), 2)
        # Combinaison du fond et des bordures
        self.bouton_Rouge_Text = self.bouton_Rouge_Fond.copy()
        self.bouton_Rouge_Text.blit(self.bouton_Rouge_Bordures, (0, 0))
    

        # Définition du bouton Jaune
        self.bouton_Jaune_Rect = pygame.Rect(150, 10, BUTTON_WIDTH, BUTTON_HEIGHT)
        # Surface pour le fond Jaune du bouton
        self.bouton_Jaune_Fond = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
        self.bouton_Jaune_Fond.fill((255, 255, 0))
        # Surface pour les bordures noires du bouton
        self.bouton_Jaune_Bordures = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.bouton_Jaune_Bordures, (0, 0, 0), self.bouton_Jaune_Bordures.get_rect(), 2)
        # Combinaison du fond et des bordures
        self.bouton_Jaune_Text = self.bouton_Jaune_Fond.copy()
        self.bouton_Jaune_Text.blit(self.bouton_Jaune_Bordures, (0, 0))
    



        # Position initiale du chapeauCowboy
        self.position_chapeauCowboy = self.chapeauCowboy.get_rect()
        self.position_chapeauCowboy.topleft = (400, 200)
        
    
        # Position initiale des lunettes de soleil
        self.position_LunettesDeSoleil = self.LunettesDeSoleil.get_rect()
        self.position_LunettesDeSoleil.topleft = (400, 100)
    
        # Position initiale du tuba
        self.position_tuba = self.tuba.get_rect()
        self.position_tuba.topleft = (400, 300)
    
        # Variables pour le suivi de l'état de déplacement de chaque accessoire
        self.en_deplacement_perso = False  
        #self.perso=self.persoRouge
        #self.position_perso=(self.perso.x,self.persoRouge.y)

          

    # Boucle principale
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                     running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.play_rect.collidepoint(event.pos):
                            print("The button 'Play' has been pressed")
                            self.perso.prop_image = pygame.transform.scale(self.perso.prop_image, (personnalisedBird.HEIGHT,personnalisedBird.HEIGHT))
                            self.perso.prop_image.set_colorkey(pygame.color.Color('white'))
                            game_start = Start(self.perso.color,self.perso.prop_image,self.perso.x_prop,self.perso.y_prop)
                        elif self.bouton_Bleu_Rect.collidepoint(event.pos):
                            self.perso.changecolor(pygame.color.Color('blue')) 
                        elif self.bouton_Jaune_Rect.collidepoint(event.pos):
                            self.perso.changecolor(pygame.color.Color('white'))
                        elif self.bouton_Rouge_Rect.collidepoint(event.pos):
                            self.perso.changecolor(pygame.color.Color('brown'))
                        else :
                            pass

                        if self.position_chapeauCowboy.collidepoint(event.pos):
                            self.perso.changeprop(self.chapeauCowboy,0,-10)
                        elif self.position_LunettesDeSoleil.collidepoint(event.pos):
                            self.perso.changeprop(self.LunettesDeSoleil,0,0)
                        elif self.position_tuba.collidepoint(event.pos):
                            self.perso.changeprop(self.tuba,0,0)
                        else:
                            pass

                    
        
            mouse_pos = pygame.mouse.get_pos()
            self.update_button(self.play_rect, self.play_button, mouse_pos)
            self.fenetre.blit(self.play_button, (self.play_rect.centerx - self.play_button.get_width() // 2, self.play_rect.centery - self.play_button.get_height() // 2))
        
            # Effacer l'écran
            self.fenetre.fill((0, 0, 0))
        
            # Redessiner le fond
            self.fenetre.blit(self.fond, (0, 0))

            # Afficher le bouton play
            self.fenetre.blit(self.play_button,(450,500))
        
            # Afficher le bouton bleu
            pygame.draw.rect(self.fenetre, (255, 255, 255), self.bouton_Bleu_Rect)
            text_x = self.bouton_Bleu_Rect.x + (self.bouton_Bleu_Rect.width - self.bouton_Bleu_Text.get_width()) // 2
            text_y = self.bouton_Bleu_Rect.y + (self.bouton_Bleu_Rect.height - self.bouton_Bleu_Text.get_height()) // 2
            self.fenetre.blit(self.bouton_Bleu_Text, (text_x, text_y))
        
            # Afficher le bouton Rouge
            pygame.draw.rect(self.fenetre, (255, 255, 255), self.bouton_Rouge_Rect)
            text_x = self.bouton_Rouge_Rect.x + (self.bouton_Rouge_Rect.width - self.bouton_Rouge_Text.get_width()) // 2
            text_y = self.bouton_Rouge_Rect.y + (self.bouton_Rouge_Rect.height - self.bouton_Rouge_Text.get_height()) // 2
            self.fenetre.blit(self.bouton_Rouge_Text, (text_x, text_y))
        
            # Afficher le bouton Jaune
            pygame.draw.rect(self.fenetre, (255, 255, 255), self.bouton_Jaune_Rect)
            text_x = self.bouton_Jaune_Rect.x + (self.bouton_Jaune_Rect.width - self.bouton_Jaune_Text.get_width()) // 2
            text_y = self.bouton_Jaune_Rect.y + (self.bouton_Jaune_Rect.height - self.bouton_Jaune_Text.get_height()) // 2
            self.fenetre.blit(self.bouton_Jaune_Text, (text_x, text_y))
            
            
            # Redessiner le personnage
            self.fenetre.blit(self.perso.image, self.perso.rect)
        
            
            # Redessiner les accessoires
            self.fenetre.blit(self.chapeauCowboy, self.position_chapeauCowboy)
            self.fenetre.blit(self.LunettesDeSoleil, self.position_LunettesDeSoleil)
            self.fenetre.blit(self.tuba, self.position_tuba)

            pygame.display.flip()
        
        pygame.quit()
        
    
        
        #display_custom()


