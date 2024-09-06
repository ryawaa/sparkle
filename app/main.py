from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.routes import stock
from app.ws.routes import trades
app = FastAPI()



@app.on_event("startup")
async def startup_event():
    app.include_router(stock.router, prefix="/api/v1")
    app.include_router(trades.router, prefix="/ws")
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Code to clean up on shutdown
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)