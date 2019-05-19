import numpy as np 
import talib

from helpers import date_to_milliseconds, interval_to_milliseconds
from client import Client
from trading_pairs import binance_pair


# Add your binance api key and api_secret here 
api_key = ''
api_secret = ''
connect = Client(api_key, api_secret)


for pair in binance_pair:
    print(pair, "pair")
    days20_data = []
    days100_data = []
    days50_data = []
    days30_data = []
    
    # =========================================
    klines = connect.get_historical_klines(pair, Client.KLINE_INTERVAL_1DAY, "100 days ago UTC", "now UTC")
    for data in klines:
        closing_price = float(data[4].replace(',', ''))
        days100_data.append(closing_price)
    
    days20_data = days100_data[:-20]
    days30_data = days100_data[:-30]
    days50_data = days100_data[:-50]
    
    try:
        days50_SMA = float(sum(days50_data) / len(days50_data))
        print(days50_SMA,"days50_SMA")

        days30_SMA = float(sum(days30_data) / len(days30_data))
        print(days30_SMA,"days30_SMA")

        days20_SMA = float(sum(days20_data) / len(days20_data))
        print(days20_SMA,"days20_SMA")
    except:
        pass
        print("passs")


    
