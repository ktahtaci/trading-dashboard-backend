from fastapi import FastAPI
import requests

app = FastAPI()

BASE_URL = "https://api.binance.com"

@app.get("/")
def home():
    return {"status": "Trading Dashboard API aktif"}

@app.get("/top20-24h")
def top20_24h():
    url = f"{BASE_URL}/api/v3/ticker/24hr"
    data = requests.get(url).json()

    usdt_pairs = [
        {
            "symbol": item["symbol"],
            "change": float(item["priceChangePercent"])
        }
        for item in data
        if item["symbol"].endswith("USDT")
    ]

    usdt_pairs.sort(key=lambda x: x["change"], reverse=True)
    return usdt_pairs[:20]
  
