#!/opt/homebrew/bin/python3
import pandas as pd
import pandas_ta as ta
from tools.yfinance import load

df = load('BTC-USD')
# print(df.iloc[[0]])
sma10 = ta.sma(df['Close'], length = 8)
ta.ma()
print(sma10.head(10))
