import websocket
import threading
import json
import asyncio
from fastapi import WebSocket
from app.core.config import settings
from typing import List

connected_clients: List[WebSocket] = []

async def on_message(ws, message):
    print("Client list:", connected_clients)
    for client in connected_clients:
        try: 
            await client.send_text(message)
        except Exception as e:
            print("Error sending message to client:", e)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("### WebSocket closed ###")

def on_open(ws):
    ws.send(json.dumps({'type': 'subscribe', 'symbol': 'AAPL'}))
    ws.send(json.dumps({'type': 'subscribe', 'symbol': 'AMZN'}))
    ws.send(json.dumps({'type': 'subscribe', 'symbol': 'BINANCE:BTCUSDT'}))
    ws.send(json.dumps({'type': 'subscribe', 'symbol': 'IC MARKETS:1'}))

def start_finnhub_websocket():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(f"wss://ws.finnhub.io?token={settings.FINNHUB_API_KEY}",
                                on_message=lambda ws, msg: asyncio.run(on_message(ws, msg)),
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    # Running WebSocket in a separate thread
    thread = threading.Thread(target=ws.run_forever)
    thread.start()