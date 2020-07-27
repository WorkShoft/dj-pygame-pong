import pygame
import time

import constants
import utils

from base_scene import BaseScene


class Menu(BaseScene):
    def __init__(self, screen):
        self.screen = screen

        self.logo = pygame.image.load(utils.get_resource("pygame_powered.gif"))
        self.rect = self.logo.get_rect()
        self.x = constants.SCREEN_CENTER[0] - self.rect.width / 2
        self.y = constants.SCREEN_CENTER[1] - self.rect.height / 2

        self.game_name = ""

        self.load_sound()
        self.intro_sound.play(fade_ms=2000)

        self.load_ui()

        self.time = time.time()

        self.playing_music = True

        pygame.mixer.music.play(fade_ms=20000)

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
                        f">{self.game_name}", True, constants.BUTTON_COLOR
                    )
                    self.typing_sound.play()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(self.audio_icon_rect, mouse_pos)
                if self.audio_icon_rect.collidepoint(mouse_pos):
                    pygame.mixer.music.pause() if self.playing_music else pygame.mixer.music.unpause()
                    self.playing_music = not self.playing_music

        self.update_keyboard()

    def update_keyboard(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.scene_manager.switch_scene("game", name=self.game_name)

    def load_sound(self):
        self.intro_sound = pygame.mixer.Sound(
            utils.get_resource("334261__projectsu012__coin-chime.wav")
        )
        self.typing_sound = pygame.mixer.Sound(
            utils.get_resource("194799__jim-ph__keyboard5.wav")
        )
        self.background_music = pygame.mixer.music.load(
            utils.get_resource("Synthwave7.wav")
        )

    def load_ui(self):
        self.font = pygame.font.Font(utils.get_resource("ZX-Spectrum/zxspectr.ttf"), 36)

        self.title = self.font.render("PONG", True, constants.BUTTON_COLOR)
        self.plus_button = self.font.render("Enter game", True, constants.BUTTON_COLOR)

        self.type_prompt = self.font.render(
            f"> {self.game_name}", True, constants.BUTTON_COLOR
        )

        self.plus_button_rect = self.plus_button.get_rect()
        self.title_rect = self.title.get_rect()

        self.audio_icon = pygame.image.load(
            utils.get_resource("500px-Speaker_Icon.svg.png")
        )
        self.audio_icon = pygame.transform.scale(
            self.audio_icon, (constants.AUDIO_ICON_WIDTH, constants.AUDIO_ICON_HEIGHT)
        )
        self.audio_icon_rect = self.audio_icon.get_rect()
        self.audio_icon_rect.x = constants.AUDIO_ICON_X
        self.audio_icon_rect.y = constants.AUDIO_ICON_Y

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
                (constants.SCREEN_CENTER[0] - self.title_rect.width / 2, 10),
            )

            self.screen.blit(
                self.audio_icon, (constants.AUDIO_ICON_X, constants.AUDIO_ICON_Y)
            )

    def render(self):
        self.screen.fill((255, 255, 255))
        self.render_ui()

        pygame.display.flip()

    def set_data(self):
        pass
