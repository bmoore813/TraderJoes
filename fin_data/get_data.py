import yfinance as yf
import os

symbols = ["TQQQ","SQQQ"]

if not os.path.exists("data"):
    os.mkdir('data')

for symbol in symbols:
    if not os.path.exists(f"data/{symbol}.csv"):
        data = yf.download(symbol, start="2018-01-01")
        if data.size > 0:
            data.to_csv(f"data/{symbol}.csv")
        
    

