import websocket
import threading
import json
import asyncio
from fastapi import WebSocket
from app.core.config import settings
from typing import List

connected_clients: List[WebSocket] = []
finnhub_ws: websocket.WebSocketApp = None

# WebSocket event handlers
async def on_message(ws, message):
    print("Received message from Finnhub WebSocket:", message)
    print("Forwarding message to connected clients:", connected_clients)
    for client in connected_clients:
        try:
            await client.send_text(message)
        except Exception as e:
            print("Error sending message to client:", e)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("### Finnhub WebSocket closed ###")

def on_open(ws):
    global finnhub_ws
    finnhub_ws = ws
    ws.send(json.dumps({'type': 'subscribe', 'symbol': 'AAPL'}))
    ws.send(json.dumps({'type': 'subscribe', 'symbol': 'AMZN'}))
    ws.send(json.dumps({'type': 'subscribe', 'symbol': 'BINANCE:BTCUSDT'}))
    ws.send(json.dumps({'type': 'subscribe', 'symbol': 'IC MARKETS:1'}))

def forward_message_to_finnhub(message: str):
    global finnhub_ws
    if finnhub_ws:
        finnhub_ws.send(message)
        print("Forwarded message to Finnhub:", message)
    else:
        print("Finnhub WebSocket is not connected.")

def start_finnhub_websocket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        f"wss://ws.finnhub.io?token={settings.FINNHUB_API_KEY}",
        on_message=lambda ws, msg: asyncio.run(on_message(ws, msg)),
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open

    # Run WebSocket in a separate thread
    thread = threading.Thread(target=ws.run_forever)
    thread.start()