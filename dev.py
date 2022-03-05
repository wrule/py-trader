#!/opt/homebrew/bin/python3
from datetime import datetime
import time
from numba import jit
import pandas_ta as ta
from tools.yfinance import load, to_kline_list
from numba_try.trader import Trader
from numba_try.backtester import Backtester
from numba_try.kline import KLine
from numba_try.history import History
from numba.typed import List as NBList

if __name__ == '__main__':
  df = load('BTC-USD')
  d = datetime.now()
  k = KLine(d, 0, 0, 0, 0, 0, True)
  # klines = to_kline_list(df)
  # trader = Trader()
  # tester = Backtester(trader)
  # hist = History(NBList(klines))
  # tester.test(hist)


