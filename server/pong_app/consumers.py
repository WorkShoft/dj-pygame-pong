import json

import constants

from .pong_controller import GameController, PaddleController, BallController
from .thread_pool import ThreadPool

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class PongConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        self.ball_controller = BallController()
        self.thread = None

        super().__init__(*args, **kwargs)

    def connect(self):
        self.game = self.scope["path"].strip("/").replace(" ", "_")

        if self.game not in ThreadPool.threads:
            ThreadPool.add_game(self.game, self)

        self.thread = ThreadPool.threads[self.game]

        async_to_sync(self.channel_layer.group_add)(self.game, self.channel_name)

        if not self.thread["paddle_one"]:
            self.paddle_controller = PaddleController("paddle_one")
            self.thread["paddle_one"] = True

        elif not self.thread["paddle_two"]:
            self.paddle_controller = PaddleController("paddle_two")
            self.thread["paddle_two"] = True

        if self.thread["paddle_one"] and self.thread["paddle_two"]:
            self.thread["active"] = True

        self.accept()

    def disconnect(self, close_code):
        self.thread[str(self.paddle_controller)] = False
        self.thread["active"] = False

        async_to_sync(self.channel_layer.group_discard)(self.game, self.channel_name)

    def receive(self, text_data):
        direction = json.loads(text_data).get("direction")
        self.paddle_controller.move(direction)

    def propagate_state(self):
        while True:
            if self.thread:
                if self.thread["active"]:
                    self.ball_controller.move()

                    async_to_sync(self.channel_layer.group_send)(
                        self.game,
                        {"type": "stream_state", "state": GameController.state,},
                    )

    def stream_state(self, event):
        state = event["state"]

        self.send(text_data=json.dumps(state))
