import asyncio
import websockets

async def echo(websocket, path):
    print('echo')
    async for message in websocket:
        while True:
            await websocket.send('greeting')

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, '127.0.0.1', 6090))
asyncio.get_event_loop().run_forever()
