#!/opt/homebrew/bin/python3
from cmath import nan
import pandas as pd
import pandas_ta as ta
from tools.yfinance import load
from strategy.strategy import Strategy
from strategy.twoLinesCross import TwoLinesCross
from snapshot_list import Snapshot, SnapshotList
import datetime

df1 = load('BTC-USD')
df1.ta.sma(length = 8, append = True)
df1.ta.sma(length = 44, append = True)
# for index, row in df1.iterrows():
#   print(row['Close'])

s = TwoLinesCross('SMA_8', 'SMA_44')
s.Backtesting(df1)

# print('你好，世界')

# list = SnapshotList()
# list.append(Snapshot(0))
# list.append(Snapshot(100000000000000, 1, 2, 0, 0, 2))
# list.append(Snapshot(200000000000000, 2, 2, 0, 0, 1.9))
# print(list.dataframe())
