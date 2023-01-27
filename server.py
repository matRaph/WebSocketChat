import asyncio
import json
from aiohttp import web

class ChatServer:
    def __init__(self):
        self.clients = []

    async def ws_handler(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        self.clients.append(ws)

        async for msg in ws:
            if msg.type == web.WSMsgType.text:
                data = json.loads(msg.data)
                for client in self.clients:
                    await client.send_json(data)

        self.clients.remove(ws)
        return ws

app = web.Application()
app.router.add_route('GET', '/ws', ChatServer().ws_handler)

web.run_app(app)

