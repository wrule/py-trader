#!/opt/homebrew/bin/python3
from snapshot_list import Snapshot, SnapshotList
from transaction_list import Transaction, TransactionList
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from tools.yfinance import load, download, to_dict_list
import pandas_ta as ta

df = load('BTC-USD')
df.ta.sma(length = 8, append = True)
df.ta.sma(length = 44, append = True)
hist = to_dict_list(df)
trader = Trader()
strategy = TwoLinesCross(trader, 'SMA_8', 'SMA_44')
strategy.Backtesting(hist)
trader.transactionList.dataframe().to_excel('transaction.xlsx')
trader.snapshotList.dataframe().to_excel('snapshot.xlsx')
