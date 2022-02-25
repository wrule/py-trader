#!/opt/homebrew/bin/python3
from datetime import datetime
import time
import pandas_ta as ta
from tools.yfinance import load, to_dict_list
from strategy.twoLinesCross import TwoLinesCross
from trader import Trader
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

df = load('BTC-USD')
df.ta.sma(length = 8, append = True)
df.ta.sma(length = 44, append = True)

hist = to_dict_list(df)

trader = Trader(snapshot = True)
tlc = TwoLinesCross(trader, 'SMA_8', 'SMA_44')
oldTime = datetime.now()
tlc.Backtesting(hist)
print(datetime.now() - oldTime)
print(trader.funds)
trader.transactionList.dataframe().to_excel('transaction.xlsx')
trader.snapshotList.dataframe().to_excel('snapshot.xlsx')

df = trader.snapshotList.dataframe()
# print(df)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(df.index, df['valuation']);  # Plot some data on the axes.
plt.show()

