from fastapi import FastAPI
from typing import Optional
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
def rate_in_currency(currency: str):
    res = requests.get('https://blockchain.info/ticker')
    json_mess = res.json()
    #error_text = 'Please enter one of the following values: USD, AUD, BRL, CAD, CHF, CLP, CNY, DKK, EUR, GBP, HKD, INR, ISK, JPY, KRW, NZD, PLN, RUB, SEK, SGD, THB, TRY, TWD'
    if json_mess[currency]:
        return json_mess[currency]
    #else:
        #return error_text

@app.get("/historical/{currency}")
def read_item(currency: str):
    return {"item_id": item_id, "q": q}
#def lineplot(x_data, y_data, x_label="", y_label="", title=""):
    # Create the plot object
    #_, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    #ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)

    # Label the axes and provide a title
    #ax.set_title(title)
    #ax.set_xlabel(x_label)
    #ax.set_ylabel(y_label)

@app.get("/convert")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    uvicorn.run(app)
