#!/opt/homebrew/bin/python3
import time
from numba import jit
import pandas_ta as ta
from tools.yfinance import load, to_dict_list
from numba_try.trader import Trader
from numba_try.two import Two

if __name__ == '__main__':
  df = load('BTC-USD')
  df.ta.sma(length = 8, append = True)
  df.ta.sma(length = 44, append = True)
  hist = to_dict_list(df)
  trader = Trader()
  strategy = Two(trader)
  # strategy.show()
  # oldTime = time.perf_counter()
  # testPerf(strategy)
  # print(time.perf_counter() - oldTime)


