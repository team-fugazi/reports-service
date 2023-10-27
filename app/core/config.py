# core/config.py
import os
# from dotenv import load_dotenv


origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

details = {
    "title": "Fugazi Reports API",
    "description": "Fugazi Reports API helps you do awesome stuff. 🚀",
    "version": "1.0.0",
    "contact": {
        "name": "bodeby",
        "url": "https://github.com/bodeby",
        "email": "thorbensen@gmail.com",
    }
}

fake_service_db = {
    "id": "16384b13-a8a7-462a-b038-f9dca3a8649a",
    "public": True,
    "source": "https://raw.githubusercontent.com/TeamBachelor/strategies-storage/main/SampleStrategy.yml",
    "meta": {
        "title": "arima",
        "scope": "skarp",
        "description": "ARIMA (AutoRegressive Integrated Moving Average) is a statistical model used for time series analysis and forecasting.",
        "tags": ["Auto-Regressive", "Moving Average", "Differencing"],
    },
    "attributes": {"popularity": 86, "quality": 34, "maintenance": 100},
}