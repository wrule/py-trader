#!/opt/homebrew/bin/python3
import yfinance as yf
from tools.yfinance import download, load

df = load('BTC-USD')
print(df)
