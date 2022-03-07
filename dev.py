#!/opt/homebrew/bin/python3
from numpy import append
import pandas_ta as ta
from tools.yfinance import to_dict_list
from tools.tradingview_csv import load
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import time
from random import randrange

data_df = load('BINANCE_BTCUSDT, 120_cd3a1')

if __name__ == '__main__':
  maxv = 0
  for i in range(10000):
    df = data_df.copy()
    length = randrange(2, 101)
    rsi_length = randrange(2, 101)
    k = randrange(2, 81)
    d = randrange(2, 81)
    df.ta.stochrsi(
      length = length,
      rsi_length = rsi_length,
      k = k,
      d = d,
      append = True,
    )
    hist = History(to_dict_list(df))
    trader = Trader(100, 0.0015, 0.0015)
    strategy = TwoLinesCross(trader, f'STOCHRSIk_{length}_{rsi_length}_{k}_{d}', f'STOCHRSId_{length}_{rsi_length}_{k}_{d}')
    strategy.backtesting(hist)
    valuation = trader.snapshotList.last().valuation()
    tlen = trader.transactionList.length()
    if tlen >= 400 and valuation > maxv:
      maxv = valuation
      print(i, valuation, tlen, [length, rsi_length, k, d])
  
  
  
  # df = load('BINANCE_BTCUSDT, 120_cd3a1')
  # df.ta.stochrsi(
  #   length = 35,
  #   rsi_length = 28,
  #   k = 21,
  #   d = 21,
  #   append = True,
  # )
  # hist = History(to_dict_list(df))
  # trader = Trader(100, 0.0015, 0.0015)
  # strategy = TwoLinesCross(trader, 'STOCHRSIk_35_28_21_21', 'STOCHRSId_35_28_21_21')
  # strategy.backtesting(hist)
  # print(trader.transactionList.length())
  # print(trader.snapshotList.last().valuation())
  # trader.transactionList.dataframe().to_excel('c.xlsx')
