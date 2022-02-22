#!/opt/homebrew/bin/python3
import pandas as pd
import pandas_ta as ta
from tools.yfinance import load
from strategy.strategy import Strategy

df = load('BTC-USD')
df.ta.sma(length = 8, append = True)
df.ta.sma(length = 44, append = True)
print(df.iloc[0:0])
print(len(df.index))

s = Strategy()
s.Backtesting(df)