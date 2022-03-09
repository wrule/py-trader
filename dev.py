#!/opt/homebrew/bin/python3
import pandas_ta as ta
from tools.yfinance import to_dict_list
from tools.tradingview_csv import load
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import matplotlib.pyplot as plt

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

if __name__ == '__main__':
  srsi_backtesting(49, 8, 8, 27)

