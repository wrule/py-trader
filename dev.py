#!/opt/homebrew/bin/python3
import pandas_ta as ta
from tools.yfinance import load, to_kline_list

if __name__ == '__main__':
  df = load('BTC-USD')
  klines = to_kline_list(df)
  print(klines[0])
