#!/opt/homebrew/bin/python3
from numpy import append
import pandas_ta as ta
from tools.yfinance import to_dict_list
from tools.tradingview_csv import load
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import time

if __name__ == '__main__':
  df = load('BINANCE_BTCUSDT, 120_cd3a1')
  df.ta.stochrsi(
    length = 28,
    rsi_length = 21,
    k = 14,
    d = 14,
    append = True,
  )
  hist = History(to_dict_list(df))
  trader = Trader(100, 0.001, 0.001)
  strategy = TwoLinesCross(trader, 'STOCHRSIk_28_21_14_14', 'STOCHRSId_28_21_14_14')
  strategy.backtesting(hist)
  print(trader.transactionList.length())
  print(trader.snapshotList.last().valuation())
  trader.transactionList.dataframe().to_excel('c.xlsx')
