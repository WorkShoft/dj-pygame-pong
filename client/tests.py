import websocket_client


def test_websocket_connection():
    uri = websocket_client.get_uri(game="foo")
    ws = websocket_client.connect(uri)

    assert ws.url == uri
