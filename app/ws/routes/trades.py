from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.core.websocket import connected_clients, start_finnhub_websocket

router = APIRouter()

@router.websocket("/trades")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)  

    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received from client: {data}")
    except WebSocketDisconnect:
        connected_clients.remove(websocket)  
        print("Client disconnected")

@router.get("/start-websocket")
async def start_websocket():
    """
    API to trigger the Finnhub WebSocket connection.
    """
    start_finnhub_websocket()  #
    return {"message": "WebSocket connection started"}
