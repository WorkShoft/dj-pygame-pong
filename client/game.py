import json
import pygame
import threading

import constants
import utils
import websocket_client

from paddle import Paddle
from ball import Ball
from base_scene import BaseScene


class Game(BaseScene):
    state = None

    def __init__(self, screen):
        self.screen = screen
        self.data = None
        self.connection = None

        self.paddle_one = Paddle()
        self.paddle_two = Paddle(color=(200, 0, 0))
        self.paddle_two.x = self.paddle_two.max_x
        self.ball = Ball(x=constants.SCREEN_WIDTH / 2, y=constants.SCREEN_HEIGHT / 2)

        self.setup_groups()
        self.paddle_group.add(self.paddle_one, self.paddle_two)
        self.ball_group.add(self.ball)

        self.load_ui()

        self.playing_music = True

    def set_data(self, data):
        self.data = data

        if "name" in self.data:
            uri = websocket_client.get_uri(game=self.data["name"])
            self.set_connection(uri)

    def set_connection(self, uri):
        self.connection = websocket_client.connect(uri)
        self.connection.on_open = websocket_client.on_open
        self.connection.on_message = self.on_message
        self.connection_thread = threading.Thread(target=self.connection.run_forever)
        self.connection_thread.daemon = True
        self.connection_thread.start()

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                print(self.audio_icon_rect, mouse_pos)
                if self.audio_icon_rect.collidepoint(mouse_pos):
                    pygame.mixer.music.pause() if self.playing_music else pygame.mixer.music.unpause()
                    self.playing_music = not self.playing_music

        self.update_keyboard()
        self.paddle_group.update()
        self.ball_group.update()

        self.apply_state()

    def apply_state(self):
        if Game.state:
            for sprite_name, sprite_data in Game.state.items():
                sprite = getattr(self, sprite_name, {})

                if sprite:
                    for k, v in sprite_data.items():
                        setattr(sprite, k, v)

    @staticmethod
    def on_message(connection, state):
        state_json = json.loads(state)
        Game.state = state_json

    def update_keyboard(self):
        keys = pygame.key.get_pressed()

        if self.connection:
            if keys[pygame.K_s]:
                websocket_client.move(self.connection, "down")

            elif keys[pygame.K_w]:
                websocket_client.move(self.connection, "up")

    def load_ui(self):
        self.font = pygame.font.Font(utils.get_resource("ZX-Spectrum/zxspectr.ttf"), 24)
        
        self.audio_icon = pygame.image.load(utils.get_resource("500px-Speaker_Icon.svg.png"))
        self.audio_icon = pygame.transform.scale(self.audio_icon, (constants.AUDIO_ICON_WIDTH, constants.AUDIO_ICON_HEIGHT))
        self.audio_icon_rect = self.audio_icon.get_rect()
        self.audio_icon_rect.x = constants.AUDIO_ICON_X
        self.audio_icon_rect.y = constants.AUDIO_ICON_Y        

    def render_ui(self):
        if Game.state:
            score_one = Game.state["paddle_one"]["score"]
            score_two = Game.state["paddle_two"]["score"]

            self.score = self.font.render(
                f"{score_one} {score_two}", True, constants.BUTTON_COLOR
            )
            score_rect = self.score.get_rect()
            self.screen.blit(
                self.score, (constants.SCREEN_CENTER[0] - score_rect.width / 2, 10)
            )

            self.screen.blit(
                self.audio_icon, (constants.AUDIO_ICON_X, constants.AUDIO_ICON_Y)
            )

    def render(self):
        self.screen.fill((255, 255, 255))
        self.paddle_group.draw(self.screen)
        self.ball_group.draw(self.screen)
        self.render_ui()

        pygame.display.flip()

    def setup_groups(self):
        self.paddle_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
