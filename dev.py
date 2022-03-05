#!/opt/homebrew/bin/python3
import pandas_ta as ta
from tools.yfinance import load, to_kline_list
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import time

if __name__ == '__main__':
  df = load('BTC-USD')
  for n in range(2, 201):
    df.ta.sma(length = n, append = True)
  klines = to_kline_list(df)
  index = 0
  for num in df['SMA_8']:
    klines[index].data['SMA_8'] = num
    index = index + 1
  index = 0
  for num in df['SMA_44']:
    klines[index].data['SMA_44'] = num
    index = index + 1
  hist = History(klines)
  trader = Trader()
  strategy = TwoLinesCross(trader, 'SMA_8', 'SMA_44')
  oldTime = time.perf_counter()
  for i in range(201):
    strategy.backtesting(hist)
  print(time.perf_counter() - oldTime)
  print(trader.snapshotList.last().valuation())
  print(trader.transactionList.length())
