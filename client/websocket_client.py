import json
import websocket


def get_uri(game=""):
    uri = f"ws://127.0.0.1:8000/{game}/"
    return uri


def connect(uri):
    connection = websocket.WebSocketApp(uri, on_error=on_error, on_close=on_close)

    return connection


def on_error(connection, error):
    print(error)


def on_close(connection):
    print(f"Closed connection")


def on_open(connection):
    def run(*args):
        pass


def move(connection, direction):
    if direction:
        connection.send(json.dumps({"direction": direction,},))
