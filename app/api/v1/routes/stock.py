from fastapi import APIRouter, Depends
import requests
from app.core.config import settings
from app.core.websocket import start_finnhub_websocket

router = APIRouter()

@router.get("/search")
async def lookup(query: str, exchange: str | None = None):
    """
    API to search for a stock symbol.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "q": query
    }

    if exchange:
        params["exchange"] = exchange

    response = requests.get("https://finnhub.io/api/v1/search", params=params)
    return response.json()

@router.get("/quote")
async def quote(symbol: str):
    """
    API to get a stock quote.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol
    }

    response = requests.get("https://finnhub.io/api/v1/quote", params=params)
    return response.json()
