#!/opt/homebrew/bin/python3
from numpy import append
import pandas_ta as ta
from tools.yfinance import load, to_dict_list
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import time

if __name__ == '__main__':
  df = load('BTC-USD')
  df.ta.stochrsi(
    length = 21,
    rsi_length = 21,
    k = 7,
    d = 7,
    append = True,
  )
  hist = History(to_dict_list(df))
  trader = Trader(100, 0.0015, 0.0015)
  strategy = TwoLinesCross(trader, 'STOCHRSIk_21_21_7_7', 'STOCHRSId_21_21_7_7')
  strategy.backtesting(hist)
  print(trader.transactionList.length())
  print(trader.snapshotList.last().valuation())
  trader.transactionList.dataframe().to_excel('c.xlsx')
