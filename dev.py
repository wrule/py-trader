#!/opt/homebrew/bin/python3
import time
import pandas_ta as ta
from tools.yfinance import load, to_dict_list
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross

if __name__ == '__main__':
  df = load('BTC-USD')
  df.ta.sma(length = 8, append = True)
  df.ta.sma(length = 44, append = True)
  hist = to_dict_list(df)
  trader = Trader()
  strategy = TwoLinesCross(trader, 'SMA_8', 'SMA_44')
  oldTime = time.perf_counter()
  # for i in range(20100):
  #   for j in range(2800):
  #     pass
  y = 0
  while y < 20100:
    x = 0
    while x < 2800:
      x = x + 1
    y = y + 1
    # strategy.Backtesting(hist)
  print(time.perf_counter() - oldTime)
  # print(trader.snapshotList.last().valuation())
