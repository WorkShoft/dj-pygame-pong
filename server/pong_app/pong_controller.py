import constants


class GameController:
    state = constants.INITIAL_STATE


class PaddleController:
    def __init__(self):
        self.state = GameController.state
        self.item = self.state["paddle_one"]

    def move(self, direction):
        if direction == "down" and self.item["y"] < constants.MAX_PADDLE_Y:
            self.item["y"] += 5

        elif direction == "up" and self.item["y"] > 0:
            self.item["y"] -= 5


class BallController:
    def __init__(self):
        self.state = GameController.state
        self.item = self.state["ball"]
        self.vel_x = 5
        self.vel_y = 5

    def move(self):
        if (
            self.item["y"] > constants.MAX_BALL_Y
            or self.item["y"] < constants.BALL_HEIGHT
        ):
            self.vel_y = -self.vel_y

        if (
            self.item["x"] > constants.MAX_BALL_X
            or self.item["x"] < constants.BALL_WIDTH
        ):
            self.vel_x = -self.vel_x

        self.item["x"] += self.vel_x
        self.item["y"] += self.vel_y
