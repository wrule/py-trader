#!/opt/homebrew/bin/python3
from numpy import append
import pandas_ta as ta
from tools.yfinance import load, to_dict_list
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import time

if __name__ == '__main__':
  df = load('BTC-USD')
  df.ta.stochrsi(
    length = 21,
    rsi_length = 21,
    k = 7,
    d = 7,
    append = True,
  )
  for size in range(2, 201):
    df.ta.sma(length = size, append = True)
  df['SMA_1'] = df['Close']
  hist = History(to_dict_list(df))
  trader = Trader()
  oldTime = time.perf_counter()
  for fast in range(1, 200):
    for slow in range(fast + 1, 201):
      strategy = TwoLinesCross(trader, f'SMA_{fast}', f'SMA_{slow}')
      strategy.backtesting(hist)
  print(time.perf_counter() - oldTime)
  print(trader.snapshotList.last().valuation())
  print(trader.transactionList.length())
