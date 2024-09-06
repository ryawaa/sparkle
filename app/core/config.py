import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    FINNHUB_API_KEY: str = os.getenv("FINNHUB_API_KEY")
    FINNHUB_WEBSOCKET_URL: str = "wss://ws.finnhub.io?token=" + FINNHUB_API_KEY

settings = Settings()
