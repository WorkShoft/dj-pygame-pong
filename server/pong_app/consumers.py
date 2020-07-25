import json

import constants

import threading

from .pong_controller import GameController, PaddleController, BallController

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class PongConsumer(WebsocketConsumer):
    paddle_controller = PaddleController()
    ball_controller = BallController()

    def connect(self):
        self.game = self.scope["path"].strip("/")

        async_to_sync(self.channel_layer.group_add)(self.game, self.channel_name)

        self.accept()

        self.state_thread = threading.Thread(target=self.propagate_state)
        self.state_thread.daemon = True
        self.state_thread.start()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.game, self.channel_name)

    def receive(self, text_data):
        direction = json.loads(text_data).get("direction")

        PongConsumer.paddle_controller.move(direction)

    def propagate_state(self):
        while True:
            PongConsumer.ball_controller.move()

            async_to_sync(self.channel_layer.group_send)(
                self.game, {"type": "stream_state", "state": GameController.state,}
            )

    def stream_state(self, event):
        state = event["state"]

        self.send(text_data=json.dumps(state))
