## Written with love by tobi <3 

from fastapi import FastAPI, WebSocketDisconnect, WebSocket
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse, Response
from fastapi.staticfiles import StaticFiles
import uvicorn, json, os
from typing import Optional, List
import app.libs.FileManager as FileManager

Server: FastAPI = FastAPI()

Server.mount("/resources/css", StaticFiles(directory=FileManager.CSS))
Server.mount("/resources/js", StaticFiles(directory=FileManager.JS))
Server.mount("/facivon.ico", Response(content=open(FileManager.IMGS + "/facivon.ico", "rb").read(), media_type="image/png"))
Server.mount("/files/download", StaticFiles(directory=FileManager.FILES))

@Server.get("/files")
async def files(List: Optional[bool] = False):
    if not List:
        with open(FileManager.HTML + "/files.html") as File:
            return HTMLResponse(File.read())
    files = [i for i in list(os.walk(FileManager.FILES))[0][2]]
    return JSONResponse(files)

@Server.get("/", response_class=HTMLResponse)
async def Main():
    with open(FileManager.HTML + "/main.html") as File:
        return File.read()

@Server.get("/discord", response_class=HTMLResponse)
async def discord():
    with open(FileManager.HTML + "/discordredirect.html") as File:
        return File.read()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.active_connections.append(ws)

    def disconnect(self, ws: WebSocket):
        self.active_connections.remove(ws)

    @staticmethod
    async def send_personal_message(message: str, ws: WebSocket):
        await ws.send_text(message)

    async def Error(self, ws: WebSocket, **kwargs):
        await ws.send_text(BuildData(**kwargs))
        self.active_connections.remove(ws)
        await ws.close()

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

BotWsManager = ConnectionManager()

Keys: dict = {"TestAdminKey": "Tobi",}

def BuildData(**kwargs) -> str:
    Data: dict = {}
    Data["type"] = kwargs.get("type") if kwargs.get("type") else None
    Data["data"] = kwargs.get("data") if kwargs.get("data") else None
    Data["message"] = kwargs.get("message") if kwargs.get("message") else None
    return json.dumps(Data)

def ParseData(Data: str) -> str:
    Allowed: list = ["args", "command", "target", "kwargs"]
    Data: dict = json.loads(Data)
    if type(Data) != dict: Data = {}
    Data = {k: v for k, v in Data.items() if k in Allowed}
    Data: str = BuildData(type="broadcast", data=Data, message="OK")
    return Data

@Server.websocket("/bots/ws")
async def botsWS(Websocket: WebSocket, key: Optional[str] = None):
    print(BotWsManager.active_connections)
    await BotWsManager.connect(Websocket)
    await Websocket.send_text(BuildData(type="connection", data=None, message="OK"))
    if not key:
        return await BotWsManager.Error(Websocket, type="error", data=None, message="no_key_provided")
    if not Keys.get(key):
        return await BotWsManager.Error(Websocket, type="error", data=None, message="key_invalid")
    try:
        while True:
            data = await Websocket.receive_text()
            Data = ParseData(data)
            print(Data)
            await BotWsManager.broadcast(Data)
    except WebSocketDisconnect:
        BotWsManager.disconnect(Websocket)
        await BotWsManager.broadcast(
            BuildData(type="disconnect", message=f"{Keys.get(key)} disconnected...", data=None)
        )

def run(**kwargs):
    uvicorn.run(Server, **kwargs)