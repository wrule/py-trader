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

if __name__ == '__main__':
  df = load('BINANCE_BTCUSDT, 15_3f5ca')
  df.ta.stochrsi(49, 8, 8, 27, append = True)
  hist = History(to_dict_list(df))
  spot = SpotAccount(0, 0.0015, 0.0015)
  contract = ContractAccount(100, 20, 0.001, 0.0004, 0.0002)
  trader = Trader(contract, spot)
  strategy = TwoLinesCross(trader, 'STOCHRSIk_49_8_8_27', 'STOCHRSId_49_8_8_27')
  strategy.backtesting(hist)
  print(trader.snapshotList.last().valuation)
  print(trader.snapshotList.return_ratio(12 * 30))
  print(trader.snapshotList.sharpe_ratio(12 * 30))
  x = trader.snapshotList.dataframe()['time']
  y = trader.snapshotList.dataframe()['valuation']
  fig, ax = plt.subplots()
  ax.plot(x, y)
  plt.show()
