from fastapi import FastAPI
from twstock import realtime
print("ddddd")
app = FastAPI()
@app.get('/stock')





def stock():
    """Test endpoint"""
    return realtime.get(['2330', '2836', '2834', '2832', '2823', '2838', '2887', '6005', '5880'])
