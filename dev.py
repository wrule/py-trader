#!/opt/homebrew/bin/python3
from pprint import pprint
from numpy import append
import pandas as pd
import pandas_ta as ta
from tools.yfinance import load, download
import pprint

if __name__ == '__main__':
  df = load('BTC-USD')
  strategy = ta.Strategy(
    name = 'JIMAO',
    ta = [
      { 'kind': 'sma', 'length': 8, },
      { 'kind': 'sma', 'length': 44, }
    ],
  )
  df.ta.strategy(strategy)
  print(df.tail(10))
