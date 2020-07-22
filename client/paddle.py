import pygame

import constants


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, color=None, *args, **kwargs):
        self.width = 10
        self.height = 50

        self.x = x
        self.y = y

        self.max_x = constants.SCREEN_WIDTH - self.width
        self.max_y = constants.SCREEN_HEIGHT - self.height 

        self.color = color if color else (100, 100, 100)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(100)

        self.rect = self.image.get_rect()
        
        super(Paddle, self).__init__(*args, **kwargs)

    def update(self):
        self.rect.x = self.x 
        self.rect.y = self.y

    def move(self, x=0, y=0):
        if y < 0 and self.y > 0 :
            self.y += y 

        elif y > 0 and self.y < self.max_y:
            self.y += y 
                
                     
            
