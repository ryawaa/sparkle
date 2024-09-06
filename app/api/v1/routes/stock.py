from fastapi import APIRouter, Depends
import requests
from app.core.config import settings
from app.core.websocket import start_finnhub_websocket

router = APIRouter()

@router.get("/price/{symbol}")
async def get_stock_price(symbol: str):
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={settings.FINNHUB_API_KEY}"
    response = requests.get(url)
    return response.json()


@router.get("/start-websocket")
async def start_websocket():
    """
    Endpoint to start the Finnhub WebSocket connection.
    """
    start_finnhub_websocket()
    return {"message": "WebSocket connection started"}

@router.get("/stop-websocket")
async def stop_websocket():
    """
    Endpoint to stop the Finnhub WebSocket connection.
    """
    # Code to stop the WebSocket connection
    return {"message": "WebSocket connection stopped"}