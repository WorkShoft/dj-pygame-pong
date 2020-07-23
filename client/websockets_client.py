import asyncio
import websockets


async def move(x, y):
    uri = "ws://localhost:8000"
    async with websockets.connect(uri) as websocket:
        await websocket.send(
            {"x": x, "y": y,}
        )
        await websocket.recv()
