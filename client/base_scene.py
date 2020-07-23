import sys
import pygame

class BaseScene:
    def close(self):
        pygame.quit()
        sys.exit("Closing game")

    def update(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError

    def update_keyboard(self):
        raise NotImplementedError

    def set_data(self, **data):
        raise NotImplementedError
