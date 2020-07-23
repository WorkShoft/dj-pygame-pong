import pygame
import time

import constants

from base_scene import BaseScene


class Menu:
    def __init__(self, screen):
        self.screen = screen

        self.logo = pygame.image.load("client/resources/pygame_powered.gif")
        self.rect = self.logo.get_rect()
        self.x = constants.SCREEN_CENTER[0] - self.rect.width / 2
        self.y = constants.SCREEN_CENTER[1] - self.rect.height / 2

        self.sound = pygame.mixer.Sound(
            "client/resources/334261__projectsu012__coin-chime.wav"
        )
        self.typing_sound = pygame.mixer.Sound(
            "client/resources/194799__jim-ph__keyboard5.wav"
        )

        self.sound.play(fade_ms=2000)

        self.time = time.time()

        self.title_font = pygame.font.Font(
            "client/resources/street_cred/street_cred.ttf", 64
        )
        self.font = pygame.font.Font("client/resources/street_cred/street_cred.ttf", 36)

        self.title = self.title_font.render("Pong", True, constants.BUTTON_COLOR)
        self.plus_button = self.font.render("Enter game", True, constants.BUTTON_COLOR)
        self.game_name = ""
        self.type_prompt = self.font.render(
            f"> {self.game_name}", True, constants.BUTTON_COLOR
        )

        self.plus_button_rect = self.plus_button.get_rect()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.close()
                else:
                    self.game_name += event.unicode
                    self.type_prompt = self.font.render(
                        f"> {self.game_name}", True, constants.BUTTON_COLOR
                    )
                    self.typing_sound.play()

        self.update_keyboard()

    def update_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.scene_manager.switch_scene("game", name=self.game_name)

    def render_ui(self):
        if time.time() - self.time < 3:
            self.screen.blit(self.logo, (self.x, self.y))

        else:
            self.screen.blit(
                self.plus_button,
                (
                    constants.SCREEN_CENTER[0] - self.plus_button_rect.width / 2,
                    constants.SCREEN_CENTER[1] - self.plus_button_rect.height,
                ),
            )
            self.screen.blit(
                self.type_prompt,
                (
                    constants.SCREEN_CENTER[0] - self.plus_button_rect.width / 2,
                    constants.SCREEN_CENTER[1],
                ),
            )
            self.screen.blit(
                self.title,
                (constants.SCREEN_CENTER[0] - self.plus_button_rect.width / 2, 0),
            )

    def render(self):
        self.screen.fill((255, 255, 255))
        self.render_ui()

        pygame.display.flip()

    def set_data(self):
        pass
