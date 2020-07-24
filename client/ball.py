import pygame

import constants


class Ball(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, color=None, *args, **kwargs):
        self.width = constants.BALL_WIDTH
        self.height = constants.BALL_HEIGHT

        self.x = x
        self.y = y

        self.max_x = constants.SCREEN_WIDTH - self.width
        self.max_y = constants.SCREEN_HEIGHT - self.height

        self.color = color if color else (0, 0, 0)

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()

        super(Ball, self).__init__(*args, **kwargs)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def move(self, x=0, y=0):
        if y < 0 and self.y > 0:
            self.y += y

        elif y > 0 and self.y < self.max_y:
            self.y += y
