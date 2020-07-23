import pygame

import constants

from paddle import Paddle
from ball import Ball

from base_scene import BaseScene


class Game(BaseScene):
    def __init__(self, screen):
        self.screen = screen

        self.paddle_one = Paddle()
        self.paddle_two = Paddle(color=(200, 0, 0))
        self.paddle_two.x = self.paddle_two.max_x

        self.ball = Ball(x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2)

        self.setup_groups()
        self.paddle_group.add(self.paddle_one, self.paddle_two)
        self.ball_group.add(self.ball)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()

        self.update_keyboard()
        self.paddle_group.update()
        self.ball_group.update()

    def update_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.paddle_one.move(y=1)

        elif keys[pygame.K_w]:
            self.paddle_one.move(y=-1)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.paddle_group.draw(self.screen)
        self.ball_group.draw(self.screen)

        pygame.display.flip()

    def setup_groups(self):
        self.paddle_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
