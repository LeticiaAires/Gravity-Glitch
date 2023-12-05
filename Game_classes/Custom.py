
import pygame
from pygame.locals import *
import os


from ModeChoice import ModeMenu

class Custom() :
    def __init__(self): 
        super().__init__()
        self.SCREEN_WIDTH_CUSTOM = 800
        self.SCREEN_HEIGHT_CUSTOM = 600
        # Définition du bouton bleu
        self.BUTTON_WIDTH = 50
        self.BUTTON_HEIGHT = 50
        self.fenetre = pygame.display.set_mode((self.SCREEN_WIDTH_CUSTOM, self.SCREEN_HEIGHT_CUSTOM))        

        self.fond = pygame.image.load('Assets/background2.jpg')
        self.fenetre.blit(self.fond, (0, 0))
        self.font_filename = "your_font.ttf"
        self.font_path = os.path.join("Assets", self.font_filename)
        #return button
        self.return_font = pygame.font.Font(self.font_path, 30)
        self.return_button = self.return_font.render("Return ", True, (0, 0, 0))
        self.return_rect = pygame.Rect((self.SCREEN_WIDTH_CUSTOM - self.BUTTON_WIDTH) // 8, 500, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)

        #continue button
        self.continue_font = pygame.font.Font(self.font_path, 30)
        self.continue_button = self.continue_font.render("Continue ", True, (0, 0, 0))
        self.continue_rect = pygame.Rect((self.SCREEN_WIDTH_CUSTOM - self.BUTTON_WIDTH) - 100, 500, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)





        # Chargement des personnages
        self.persoRouge = pygame.image.load("Assets/FlappyBird0.png").convert_alpha()
        self.nouvelle_taille = (90, 90)
        self.persoRouge = pygame.transform.scale(self.persoRouge, self.nouvelle_taille)
        self.position_persoRouge = self.persoRouge.get_rect()
        self.position_persoRouge.topleft = (100, 300)    
        self.persoJaune = pygame.image.load("Assets/bird1.png").convert_alpha()
        self.persoJaune = pygame.transform.scale(self.persoJaune, self.nouvelle_taille)
        self.persoJaune.set_colorkey((255, 255, 255))

        self.persoBleu = pygame.image.load("Assets/OiseauBleu.png").convert_alpha()
        self.persoBleu = pygame.transform.scale(self.persoBleu, self.nouvelle_taille)
        self.persoBleu.set_colorkey((255, 255, 255))
        
        



            # Chargement des accessoires
        self.chapeauCowboy = pygame.image.load("Assets/chapeau_cowboy.png").convert_alpha()
        self.chapeauCowboy = pygame.transform.scale(self.chapeauCowboy, self.nouvelle_taille)
        
        self.LunettesDeSoleil = pygame.image.load("Assets/lunettes-de-soleil.jpg").convert_alpha()
        self.LunettesDeSoleil = pygame.transform.scale(self.LunettesDeSoleil, self.nouvelle_taille)
        self.LunettesDeSoleil.set_colorkey((253, 253, 253))
        self.tuba = pygame.image.load("Assets/tuba.jpg").convert_alpha()
        self.tuba = pygame.transform.scale(self.tuba, self.nouvelle_taille)
        self.tuba.set_colorkey((255, 255, 255))



            #Différentes combinaisons
        self.RougeLunettes= pygame.image.load("Assets/RougeLunettes.png").convert_alpha()
        self.RougeLunettes= pygame.transform.scale(self.RougeLunettes, self.nouvelle_taille)
        
        self.RougeChapeau= pygame.image.load("Assets/RougeChapeau.png").convert_alpha()
        self.RougeChapeau= pygame.transform.scale(self.RougeChapeau, self.nouvelle_taille)
        
        self.RougeTuba= pygame.image.load("Assets/RougeTuba.png").convert_alpha()
        self.RougeTuba= pygame.transform.scale(self.RougeTuba, self.nouvelle_taille)
        
        self.BleuLunettes= pygame.image.load("Assets/BleuLunettes.png").convert_alpha()
        self.BleuLunettes= pygame.transform.scale(self.BleuLunettes, self.nouvelle_taille)
        
        self.BleuChapeau= pygame.image.load("Assets/BleuChapeau.png").convert_alpha()
        self.BleuChapeau= pygame.transform.scale(self.BleuChapeau, self.nouvelle_taille)
        
        self.BleuTuba= pygame.image.load("Assets/BleuTuba.png").convert_alpha()
        self.BleuTuba= pygame.transform.scale(self.BleuTuba, self.nouvelle_taille)
        
        self.JauneLunettes= pygame.image.load("Assets/JauneLunettes.png").convert_alpha()
        self.JauneLunettes= pygame.transform.scale(self.JauneLunettes, self.nouvelle_taille)
        
        self.JauneChapeau= pygame.image.load("Assets/JauneChapeau.png").convert_alpha()
        self.JauneChapeau= pygame.transform.scale(self.JauneChapeau, self.nouvelle_taille)
        
        self.JauneTuba= pygame.image.load("Assets/JauneTuba.png").convert_alpha()
        self.JauneTuba= pygame.transform.scale(self.JauneTuba, self.nouvelle_taille)



        self.bouton_Bleu_Rect = pygame.Rect((self.SCREEN_WIDTH_CUSTOM - self.BUTTON_WIDTH) // 2, 10, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            # Surface pour le fond bleu du bouton
        self.bouton_Bleu_Fond = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.bouton_Bleu_Fond.fill((0, 0, 255))
            # Surface pour les bordures noires du bouton
        self.bouton_Bleu_Bordures = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.bouton_Bleu_Bordures, (0, 0, 0), self.bouton_Bleu_Bordures.get_rect(), 2)
        # Combinaison du fond et des bordures
        self.bouton_Bleu_Text = self.bouton_Bleu_Fond.copy()
        self.bouton_Bleu_Text.blit(self.bouton_Bleu_Bordures, (0, 0))
            # Définition du bouton rouge
        self.bouton_Rouge_Rect = pygame.Rect(self.SCREEN_WIDTH_CUSTOM - self.BUTTON_WIDTH - 150, 10, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            # Surface pour le fond rouge du bouton
        self.bouton_Rouge_Fond = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.bouton_Rouge_Fond.fill((255, 0, 0))
            # Surface pour les bordures noires du bouton
        self.bouton_Rouge_Bordures = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(self.bouton_Rouge_Bordures, (0, 0, 0), self.bouton_Rouge_Bordures.get_rect(), 2)
            # Combinaison du fond et des bordures
        self.bouton_Rouge_Text = self.bouton_Rouge_Fond.copy()
        self.bouton_Rouge_Text.blit(self.bouton_Rouge_Bordures, (0, 0))
            # Définition du bouton Jaune
        self.bouton_Jaune_Rect = pygame.Rect(150, 10, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
            # Surface pour le fond Jaune du bouton
        self.bouton_Jaune_Fond = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_HEIGHT))
        self.bouton_Jaune_Fond.fill((255, 255, 0))
            # Surface pour les bordures noires du bouton
        self.bouton_Jaune_Bordures = pygame.Surface((self.BUTTON_WIDTH, self.BUTTON_HEIGHT), pygame.SRCALPHA)
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
        self.en_deplacement_chapeauCowboy = False
        self.en_deplacement_LunettesDeSoleil = False
        self.en_deplacement_tuba = False
        self.en_deplacement_perso = False  

        self.perso=self.persoRouge
        self.position_perso=self.position_persoRouge
    def run(self):
        # Boucle principale
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.return_rect.collidepoint(mouse_pos):
                        print("The button 'Return' has been pressed")
                        running = False
                        return "main"
                    elif self.continue_rect.collidepoint(mouse_pos):
                        print("The button 'Continue' has been pressed")
                        mode_menu=ModeMenu()
                        mode_menu.run()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.bouton_Bleu_Rect.collidepoint(event.pos):
                                self.perso = self.persoBleu
                                self.position_perso = self.position_persoRouge
                        elif self.bouton_Rouge_Rect.collidepoint(event.pos):
                                self.perso = self.persoRouge
                                self.position_perso = self.position_persoRouge
                        elif self.bouton_Jaune_Rect.collidepoint(event.pos):
                                self.perso = self.persoJaune
                                self.position_perso = self.position_persoRouge
                        elif self.position_chapeauCowboy.collidepoint(event.pos):
                                self.en_deplacement_chapeauCowboy = True
                                self.offset_x, self.offset_y = self.position_chapeauCowboy.topleft[0] - event.pos[0], self.position_chapeauCowboy.topleft[1] - event.pos[1]
                        elif self.position_LunettesDeSoleil.collidepoint(event.pos):
                                self.en_deplacement_LunettesDeSoleil = True
                                self.offset_x, offset_y = self.position_LunettesDeSoleil.topleft[0] - event.pos[0], self.position_LunettesDeSoleil.topleft[1] - event.pos[1]
                        elif self.position_tuba.collidepoint(event.pos):
                                self.en_deplacement_tuba = True
                                self.offset_x, offset_y = self.position_tuba.topleft[0] - event.pos[0], self.position_tuba.topleft[1] - event.pos[1]
                        elif self.position_perso.collidepoint(event.pos):
                                self.en_deplacement_perso = True
                                self.offset_x, self.offset_y = self.position_perso.topleft[0] - event.pos[0], self.position_perso.topleft[1] - event.pos[1]
                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        self.en_deplacement_chapeauCowboy = False
                        self.en_deplacement_LunettesDeSoleil = False
                        self.en_deplacement_tuba = False
                        self.en_deplacement_perso = False
                        if self.en_deplacement_chapeauCowboy:
                            if self.perso == self.persoJaune:
                                    self.perso = self.JauneChapeau
                            elif self.perso == self.persoBleu:
                                    self.perso = self.BleuChapeau
                            elif self.perso == self.persoRouge:
                                    self.perso = self.RougeChapeau
                        elif self.en_deplacement_LunettesDeSoleil:
                            if self.perso == self.persoJaune:
                                    self.perso = self.JauneLunettes
                            elif self.perso == self.persoBleu:
                                    self.perso = self.BleuLunettes
                            elif self.perso == self.persoRouge:
                                    self.perso = self.RougeLunettes
                        elif self.en_deplacement_tuba:
                            if self.perso == self.persoJaune:
                                    self.perso = self.JauneTuba
                            elif self.perso == self.persoBleu:
                                    self.perso = self.BleuTuba
                            elif self.perso == self.persoRouge:
                                    self.perso = self.RougeTuba

                elif event.type == MOUSEMOTION:
                    if self.en_deplacement_chapeauCowboy:
                            self.position_chapeauCowboy.topleft = (event.pos[0] + self.offset_x, event.pos[1] + offset_y)
                    elif self.en_deplacement_LunettesDeSoleil:
                            self.position_LunettesDeSoleil.topleft = (event.pos[0] + self.offset_x, event.pos[1] + offset_y)
                    elif self.en_deplacement_tuba:
                            self.position_tuba.topleft = (event.pos[0] + self.offset_x, event.pos[1] + offset_y)
                    elif self.en_deplacement_perso:
                            self.position_perso.topleft = (event.pos[0] + self.offset_x, event.pos[1] + offset_y)
        
                mouse_pos1 = pygame.mouse.get_pos()
                self.update_button(self.return_rect, self.return_button, mouse_pos1)
                self.update_button(self.continue_rect, self.continue_button, mouse_pos1)
        
                # Effacer l'écran
                self.fenetre.fill((0, 0, 0))
        
                # Redessiner le fond
                self.fenetre.blit(self.fond, (0, 0))
        
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
                self.fenetre.blit(self.perso, self.position_perso)
        
                # Redessiner les accessoires
                self.fenetre.blit(self.chapeauCowboy, self.position_chapeauCowboy)
                self.fenetre.blit(self.LunettesDeSoleil, self.position_LunettesDeSoleil)
                self.fenetre.blit(self.tuba, self.position_tuba)

                #afficher les boutons
                self.fenetre.blit(self.return_button, (self.return_rect.centerx - self.return_button.get_width() // 2, self.return_rect.centery - self.return_button.get_height() // 2))
                self.fenetre.blit(self.continue_button, (self.continue_rect.centerx - self.continue_button.get_width() // 2, self.continue_rect.centery - self.continue_button.get_height() // 2))
        
            pygame.display.flip()


#Function to increase the size of a button when the mouse is on it 
    def update_button(self, button_rect, button_surface, mouse_pos):
        if button_rect.collidepoint(mouse_pos):
            button_rect.w = self.BUTTON_WIDTH + 20
            button_rect.h = self.BUTTON_HEIGHT + 10
        else:
            button_rect.w = self.BUTTON_WIDTH
            button_rect.h = self.BUTTON_HEIGHT