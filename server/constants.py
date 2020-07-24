SCREEN_WIDTH = 700
SCREEN_HEIGHT = 450

SCREEN_CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

BUTTON_COLOR = (0, 0, 0)

PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50

MAX_PADDLE_X = SCREEN_WIDTH - PADDLE_WIDTH
MAX_PADDLE_Y = SCREEN_HEIGHT - PADDLE_HEIGHT

BALL_WIDTH = 10
BALL_HEIGHT = 10

MAX_BALL_X = SCREEN_WIDTH - BALL_WIDTH
MAX_BALL_Y = SCREEN_HEIGHT - BALL_HEIGHT

INITIAL_STATE = {
    "paddle_one": {"x": 0, "y": 0,},
    "paddle_two": {"x": SCREEN_WIDTH - PADDLE_WIDTH, "y": 0,},
    "ball": {"x": SCREEN_CENTER[0], "y": BALL_HEIGHT,},
}
