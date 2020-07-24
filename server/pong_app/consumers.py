import json

import constants

import threading

from .pong_controller import GameController, PaddleController, BallController
from channels.generic.websocket import WebsocketConsumer


class PongConsumer(WebsocketConsumer):
    paddle_controller = PaddleController()
    ball_controller = BallController()

    def connect(self):
        self.accept()

        # self.state_thread = threading.Thread(target=self.stream_state)
        # self.state_thread.daemon = True
        # self.state_thread.start()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        direction = json.loads(text_data).get("direction")

        PongConsumer.paddle_controller.move(direction)
        PongConsumer.ball_controller.move()

        self.send(text_data=json.dumps(GameController.state))

    def stream_state(self):
        while True:
            self.send(text_data=json.dumps(GameController.state))
