from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Simple Time API")

@app.get("/")
async def root():
    return {
        "message": "Сервер работает",
        "docs_url": "/docs"
    }

@app.get("/time")
async def get_server_time():
    """Возвращает текущее время сервера."""
    now = datetime.now()
    return {
        "iso_format": now.isoformat(),
        "timestamp": now.timestamp(),
        "readable": now.strftime("%Y-%m-%d %H:%M:%S")
    }

