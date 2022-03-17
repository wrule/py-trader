#!/opt/homebrew/bin/python3
from numpy import append
from account.contract_account import ContractAccount
from account.spot_account import SpotAccount
from snapshot_list import Snapshot, SnapshotList
from tools.tradingview_csv import load
from tools.yfinance import to_dict_list
from strategy.history import History
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.twoLinesCrossSpot import TwoLinesCrossSpot
import pandas_ta as ta
import matplotlib.pyplot as plt
import numpy as np
from random import randrange

df_src = load('BINANCE_BTCUSDT, 15_3f5ca')

def test(a: int, b: int, c: int, d: int):
  df = df_src.copy()
  df.ta.stochrsi(
    length = 49,
    rsi_length = 8,
    k = 8,
    d = 27,
    append = True,
  )
  df.to_excel('df.xlsx')
  hist = History(df)
  hist.show_transaction()
  spot = SpotAccount(0, 0.0015, 0.0015)
  contract = ContractAccount(100, 20, 0.001, 0.0004, 0.0002)
  trader = Trader(contract, spot)
  strategy = TwoLinesCross(trader, f'STOCHRSIk_{a}_{b}_{c}_{d}', f'STOCHRSId_{a}_{b}_{c}_{d}')
  strategy.backtesting(hist)
  # print(trader.transactionList.length())
  trader.transactionList.dataframe().to_excel('out.xlsx')
  return trader.snapshotList.last().valuation

if __name__ == '__main__':
  test(49, 8, 8, 27)
  # print(test(49, 8, 8, 27))
  # max = 0
  # while True:
  #   a = randrange(2, 100)
  #   b = randrange(2, 100)
  #   c = randrange(2, 100)
  #   d = randrange(2, 100)
  #   result = test(a, b, c, d)
  #   if result > 90:
  #     print(a, b, c, d, result)

