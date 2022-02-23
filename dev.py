#!/opt/homebrew/bin/python3
import pandas as pd
import pandas_ta as ta
from tools.yfinance import load
from strategy.strategy import Strategy
from strategy.twoLinesCross import TwoLinesCross

df = load('BTC-USD')
df.ta.sma(length = 8, append = True)
df.ta.sma(length = 44, append = True)
print(len(df.index))

print(df.iloc[0]['Close'])

s = TwoLinesCross()
s.Backtesting(df)
