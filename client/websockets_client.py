import asyncio
import websockets


class WebsocketsClient():
    def __init__(game):
        self.uri = f"ws://localhost:8000/{game}/"

    async def connect(self):
        self.connection = await websockets.client.connect(self.uri)
        
    async def move(self, direction):
        await self.connection.send(
            {"direction": direction, }
        )
        
        await self.connection.recv()
