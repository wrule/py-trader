#!/opt/homebrew/bin/python3
from numpy import sctype2char
import pandas_ta as ta
from tools.yfinance import to_dict_list
from tools.tradingview_csv import load
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import matplotlib.pyplot as plt
from stock.spot import Spot
from stock.short import Short

src_df = load('BINANCE_BTCUSDT, 120_cd3a1')

def srsi_backtesting(
  length: int,
  rsi_length: int,
  k: int,
  d: int,
):
  df = src_df.copy()
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
  snapshot_df = trader.snapshotList.dataframe()
  valuation = trader.snapshotList.last().valuation()
  print(valuation)
  print(trader.snapshotList.return_ratio(size = 12 * 4))
  print(trader.snapshotList.return_ratio_std(size = 12 * 4))
  print(trader.snapshotList.sharpe_ratio(size = 12 * 4))
  fig, ax = plt.subplots()
  ax.plot(snapshot_df['time'], snapshot_df['valuation'])
  # plt.show()
def baozhengjin(
  lever: int,
  usdt: float,
  price: float,
  smallest_unit: float,
  new_price: float,
):
  assetsNum = int(usdt / price / smallest_unit) * smallest_unit
  print('资产', assetsNum)
  fundsNum = assetsNum * price
  print('资金', fundsNum)
  bzj = fundsNum / lever
  print('保证金', bzj)

if __name__ == '__main__':
  stock = Short(
    0.003,
    { 'Date': None, 'Close': 39340.0 },
    20,
  )
  # print(stock.start_valuation())


