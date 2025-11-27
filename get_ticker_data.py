import os
from datetime import datetime, timedelta
import time
import yfinance as yf

with open('target_directory.txt', 'r') as f:
    directory = f.read()

# create working directory
if not os.path.exists(directory):
    os.makedirs(directory)

date_obj = datetime.strptime(directory, '%Y-%m-%d')
print(date_obj + timedelta(days=1))
start_date_str = (date_obj - timedelta(days=15)).strftime('%Y-%m-%d')
end_date_str = (date_obj + timedelta(days=1)).strftime('%Y-%m-%d')


def get_ticker_history(stock_symbol):
    ticker = yf.Ticker(stock_symbol)
    data = ticker.history(start=start_date_str, end=end_date_str)
    data.to_csv(f'{directory}/{stock_symbol.lower()}.csv', index=True)
    time.sleep(0.5)
    return data


df = get_ticker_history('DIA')
print(df.tail())