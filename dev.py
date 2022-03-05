#!/opt/homebrew/bin/python3
import pandas_ta as ta
from tools.yfinance import load, to_kline_list
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import time

if __name__ == '__main__':
  df = load('BTC-USD')
  klines = to_kline_list(df)
  hist = History(klines)
  trader = Trader()
  strategy = TwoLinesCross(trader, '', '')
  oldTime = time.perf_counter()
  for i in range(20100):
    strategy.backtesting(hist)
  print(time.perf_counter() - oldTime)
  print(trader.snapshotList.last().valuation())
  print(trader.transactionList.length())
