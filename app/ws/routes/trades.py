from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.core.websocket import connected_clients, start_finnhub_websocket, forward_message_to_finnhub
from typing import List

router = APIRouter()

@router.websocket("/trades")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    print("Client connected:", websocket)

    try:
        while True:
            data = await websocket.receive_text()
            print("Received message from client:", data)
            # Forwarding message from client to Finnhub
            forward_message_to_finnhub(data)
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
        print("Client disconnected:", websocket)

@router.get("/start-websocket")
async def start_websocket():
    """
    API to trigger the Finnhub WebSocket connection.
    """
    start_finnhub_websocket()
    return {"message": "WebSocket connection to Finnhub started"}