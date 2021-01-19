from fastapi import FastAPI
from typing import Optional
from bs4 import BeautifulSoup
import uvicorn
import json
import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/now")
def rate_now():
    res = requests.get('https://blockchain.info/ticker')
    if res:
        print('Response OK')
    else:
        print('Response Failed')
    json_mess = res.json()
    return json_mess

@app.get("/now/{currency}")
def rate_in_currency(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/historical/{currency}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/convert")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app)
