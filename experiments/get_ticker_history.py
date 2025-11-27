import yfinance as yf
import time

start_date_str = '2025-11-20'
end_date_str = '2025-11-26'


# For close price for target date and one day prior
def get_ticker_history(stock_symbol):
    ticker = yf.Ticker(stock_symbol)
    data = ticker.history(start=start_date_str, end=end_date_str)
    time.sleep(0.5)
    return data


df = get_ticker_history('YM=F')
print(df)
print('profit/loss', df['Close'].iloc[1] - df['Close'].iloc[0])