import constants

import time


class GameController:
    state = constants.INITIAL_STATE


class PaddleController:
    def __init__(self, paddle):
        """
        paddle: 'paddle_one' | 'paddle_two'
        """

        self.state = GameController.state
        self.paddle = paddle
        self.item = self.state[paddle]

    def move(self, direction):
        if direction == "down" and self.item["y"] < constants.MAX_PADDLE_Y:
            self.item["y"] += 5

        elif direction == "up" and self.item["y"] > 0:
            self.item["y"] -= 5

    def __str__(self):
        return self.paddle


class BallController:
    def __init__(self):
        self.state = GameController.state
        self.item = self.state["ball"]
        self.paddle_one = self.state["paddle_one"]
        self.paddle_two = self.state["paddle_two"]

        self.reset_ball()

        self.time = time.time()

    def reset_ball(self):
        self.vel_x = -5
        self.vel_y = 5
        self.item["x"] = constants.SCREEN_CENTER[0]
        self.item["y"] = 10

    def move(self):
        if time.time() - self.time > 0.01:
            if (
                self.item["y"] > constants.MAX_BALL_Y
                or self.item["y"] < constants.BALL_HEIGHT
            ):
                self.vel_y = -self.vel_y

            if 0 < self.item["x"] <= constants.PADDLE_WIDTH:
                if (
                    self.paddle_one["y"]
                    < self.item["y"]
                    < (self.paddle_one["y"] + constants.PADDLE_HEIGHT)
                ):
                    self.vel_x = -self.vel_x
                    self.item["x"] += 7

            elif self.item["x"] < 0:
                self.paddle_two["score"] += 1
                self.reset_ball()

            elif constants.SCREEN_WIDTH > self.item["x"] >= constants.MAX_BALL_X:
                if (
                    self.paddle_two["y"]
                    < self.item["y"]
                    < (self.paddle_two["y"] + constants.PADDLE_HEIGHT)
                ):
                    self.vel_x = -self.vel_x
                    self.item["x"] -= 7

            elif self.item["x"] >= constants.SCREEN_WIDTH:
                self.paddle_one["score"] += 1
                self.reset_ball()

            self.item["x"] += self.vel_x
            self.item["y"] += self.vel_y

            self.time = time.time()
