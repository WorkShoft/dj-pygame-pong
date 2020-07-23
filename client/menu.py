import sys
import pygame

import constants


class Menu:
    def __init__(self, screen):
        self.screen = screen

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()

        self.update_keyboard()

    def update_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.scene_manager.switch_scene("game")

    def render(self):
        self.screen.fill((210, 210, 210))

    def close(self):
        pygame.quit()
        sys.exit("Closing game")
