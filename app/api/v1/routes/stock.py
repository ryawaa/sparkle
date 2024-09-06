from fastapi import APIRouter, HTTPException
import requests
from app.core.config import settings
import datetime as dt

router = APIRouter()

FINNHUB_BASE_URL = "https://finnhub.io/api/v1"


def handle_response(response):
    try:
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise HTTPException(status_code=response.status_code, detail=str(e))


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

    response = requests.get(f"{FINNHUB_BASE_URL}/search", params=params)
    return handle_response(response)


@router.get("/quote")
async def quote(symbol: str):
    """
    API to get a stock quote.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/quote", params=params)
    return handle_response(response)


@router.get("/profile")
async def profile(symbol: str):
    """
    API to get company profile.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/stock/profile2", params=params)
    return handle_response(response)


@router.get("/peers")
async def peers(symbol: str):
    """
    API to get company peers.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/stock/peers", params=params)
    return handle_response(response)


@router.get("/company-news")
async def company_news(symbol: str):
    """
    API to get company news.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol,
        "to": dt.datetime.now().strftime("%Y-%m-%d"),
        "from": (dt.datetime.now() - dt.timedelta(days=7)).strftime("%Y-%m-%d")
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/company-news", params=params)
    return handle_response(response)


@router.get("/basic-financials")
async def basic_financials(symbol: str):
    """
    API to get basic financials.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol,
        "metric": "all"
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/stock/metric", params=params)
    return handle_response(response)


@router.get("/insider-transactions")
async def insider_transactions(symbol: str):
    """
    API to get insider transactions.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/stock/insider-transactions", params=params)
    return handle_response(response)


@router.get("/insider-sentiments")
async def insider_sentiments(symbol: str):
    """
    API to get insider sentiments.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol,
        "to": dt.datetime.now().strftime("%Y-%m-%d"),
        "from": (dt.datetime.now() - dt.timedelta(days=7)).strftime("%Y-%m-%d")
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/stock/insider-sentiment", params=params)
    return handle_response(response)


@router.get("/financials-as-reported")
async def financials_as_reported(symbol: str):
    """
    API to get financials as reported.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/stock/financials-reported", params=params)
    return handle_response(response)


@router.get("/ipos")
async def ipos():
    """
    API to get IPO calendar.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "from": dt.datetime.now().strftime("%Y-%m-%d"),
        "to": (dt.datetime.now() + dt.timedelta(days=7)).strftime("%Y-%m-%d")
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/calendar/ipo", params=params)
    return handle_response(response)


@router.get("/recommendation-trends")
async def recommendation_trends(symbol: str):
    """
    API to get recommendation trends.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/stock/recommendation", params=params)
    return handle_response(response)


@router.get("/history-surprise")
async def history_surprise(symbol: str):
    """
    API to get earnings surprise.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "symbol": symbol
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/stock/earnings", params=params)
    return handle_response(response)


@router.get("/earnings-calendar")
async def earnings_calendar():
    """
    API to get earnings calendar.
    """
    params = {
        "token": settings.FINNHUB_API_KEY,
        "from": dt.datetime.now().strftime("%Y-%m-%d"),
        "to": (dt.datetime.now() + dt.timedelta(days=7)).strftime("%Y-%m-%d")
    }

    response = requests.get(f"{FINNHUB_BASE_URL}/calendar/earnings", params=params)
    return handle_response(response)