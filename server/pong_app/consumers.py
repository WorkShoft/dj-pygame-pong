import json

import constants

from .pong_controller import GameController, PaddleController, BallController
from .thread_pool import ThreadPool

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class PongConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        self.ball_controller = BallController()

        super().__init__(*args, **kwargs)

    def connect(self):
        self.game = self.scope["path"].strip("/")

        async_to_sync(self.channel_layer.group_add)(self.game, self.channel_name)
        self.accept()

        if self.game not in ThreadPool.threads:
            ThreadPool.add_game(self.game, self)

        ThreadPool.threads[self.game]["player_count"] += 1

        if ThreadPool.threads[self.game]["player_count"] == 1:
            self.paddle_controller = PaddleController("paddle_one")

        else:
            self.paddle_controller = PaddleController("paddle_two")

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.game, self.channel_name)

    def receive(self, text_data):
        direction = json.loads(text_data).get("direction")

        self.paddle_controller.move(direction)

    def propagate_state(self):
        while True:
            self.ball_controller.move()

            async_to_sync(self.channel_layer.group_send)(
                self.game, {"type": "stream_state", "state": GameController.state,}
            )

    def stream_state(self, event):
        state = event["state"]

        self.send(text_data=json.dumps(state))
