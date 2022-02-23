#!/opt/homebrew/bin/python3
from cmath import nan
import pandas as pd
import pandas_ta as ta
from tools.yfinance import load
from strategy.strategy import Strategy
from strategy.twoLinesCross import TwoLinesCross
from snapshot_list import SnapshotList
import datetime

df1 = load('BTC-USD')
# df.ta.sma(length = 8, append = True)
# df.ta.sma(length = 44, append = True)

# s = TwoLinesCross('SMA_8', 'SMA_44')
# s.Backtesting(df)

print('你好，世界')

list = SnapshotList()
list.append({})