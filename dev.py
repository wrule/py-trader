#!/opt/homebrew/bin/python3
import yfinance as yf

msft = yf.Ticker('BTC-USD')
hist = msft.history(period = 'max')
print(hist)
