from twstock import realtime
from fastapi import FastAPI, Query
from typing import List
app = FastAPI()

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


@app.get('/stock')

def stock(id_list: List[str] = Query(None)):
    return _format_stock_info(realtime.get(id_list))
