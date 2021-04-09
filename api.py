from twstock import realtime
from fastapi import FastAPI, Request
from typing import List
from pydantic import BaseModel
app = FastAPI()

class Item(BaseModel):
    id_list: list


def _format_stock_info(data) -> dict:
    result = []
    if 'success' in data: del data['success']
    for x in data:
        result.append({
            'Code': data[x]['info']['code'],
            'Name': data[x]['info']['name'],
            'Open': data[x]['realtime']['open'],
            'High': data[x]['realtime']['high'],
            'Low': data[x]['realtime']['low'],
            'Last': data[x]['realtime']['latest_trade_price'],
            'SendTime': data[x]['info']['time'],
        })

    return result


@app.post('/stock')

def stock(item: Item):
    return _format_stock_info(realtime.get(item.id_list))
