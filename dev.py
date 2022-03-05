#!/opt/homebrew/bin/python3
from datetime import datetime
import time
from numba import jit
import pandas_ta as ta
from tools.yfinance import load, to_kline_list
from numba_try.trader import Trader
from numba_try.backtester import Backtester
from numba_try.history import History
from numba.typed import List as NBList
from numba import jit

@jit
def kkk():
  lastIndex = 0
  for y in range(20100):
    for x in range(2724):
      lastIndex = x * y

if __name__ == '__main__':
  df = load('BTC-USD')
  klines = to_kline_list(df)
  trader = Trader()
  tester = Backtester(trader)
  hist = History(NBList(klines))
  oldTime = time.perf_counter()
  tester.test(hist)
  # kkk()
  print(time.perf_counter() - oldTime)


