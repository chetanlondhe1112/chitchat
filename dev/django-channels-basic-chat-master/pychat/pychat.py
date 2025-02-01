import asyncio
import websockets
import json

async def chat():
    uri = "ws://127.0.0.1:8000/ws/socket-server/"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps({
            'message': 'Hello, this is a private message!',
        }))
        
        response = await websocket.recv()
        print(f"< {response}")

asyncio.run(chat())
