import pygame
from Bird import Bird

class personnalisedBird(Bird) :
    def __init__(self, x, y, msec_to_climb, images,color,prop_image,x_prop,y_prop):
         
        super(personnalisedBird, self).__init__(x, y, msec_to_climb, images)

        self.original_images = (self._img_wingup.copy(),self._img_wingdown.copy())

        self.color = color
        self.prop_image= prop_image
        self.x_prop = x_prop
        self.y_prop = y_prop

        self.changecolor(color)
        self.changeprop(prop_image,x_prop,y_prop)

    


    def changecolor (self, color):
        self.color = color
        
        #generate a color mask of the same size of the _img_wing*** images
        colorMask = pygame.Surface(self._img_wingup.get_size()).convert_alpha()
        colorMask.fill(color)

        #reset the images
        alphaMask = pygame.Surface(self._img_wingup.get_size(),pygame.SRCALPHA,32)
        self._img_wingup = alphaMask
        self._img_wingdown  = alphaMask
        self._img_wingup.blit(self.original_images[0],(0,0))
        self._img_wingdown.blit(self.original_images[1],(0,0))
        #Blend the _img_wing*** with the color masks to apply the color to the sprite.
        self._img_wingup.blit(colorMask, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
        self._img_wingdown.blit(colorMask, (0,0), special_flags = pygame.BLEND_RGBA_MULT)

   
    
    def changeprop (self, prop_image,x_prop,y_prop):
        if (prop_image != None):
            self.prop_image= prop_image
            self.x_prop = x_prop
            self.y_prop = y_prop
            self.changecolor(self.color)
            #Add prop to the bird
            self._img_wingup.blit(prop_image,(x_prop,y_prop))
            self._img_wingdown.blit(prop_image,(x_prop,y_prop))
