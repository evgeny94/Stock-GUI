import yfinance as yf

aapl= yf.Ticker("aapl")
aapl

aapl_historical = aapl.history(start="2020-06-02", end="2020-06-07", interval="1m")
aapl_historical