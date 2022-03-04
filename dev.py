#!/opt/homebrew/bin/python3
import time
from numba import jit
import pandas_ta as ta
from tools.yfinance import load, to_dict_list
from numba_try.trader import Trader
from numba_try.backtester import Backtester
from numba_try.kline import KLine
from numba_try.history import History
from numba.typed import List as NBList

if __name__ == '__main__':
  df = load('BTC-USD')
  df.ta.sma(length = 8, append = True)
  df.ta.sma(length = 44, append = True)
  hist = to_dict_list(df)
  trader = Trader()
  tester = Backtester(trader)
  kline = KLine(0, 0, 0, 0, 0, 0, False)
  hist = History(NBList([kline, kline, kline]))
  tester.test(hist)


