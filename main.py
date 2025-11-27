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

@app.get("/date")
async def get_server_date():
    """Возвращает текущую дату сервера."""
    today = datetime.now().date()
    return {
        "iso_format": today.isoformat(),
        "readable": today.strftime("%Y-%m-%d")
    }

@app.get("/datetime")
async def get_server_datetime():
    """Возвращает суммарную информацию с эндпоинтов /time и /date."""
    time_response = await get_server_time()
    date_response = await get_server_date()
    return {
        "time_info": time_response,
        "date_info": date_response
    }

