#!/opt/homebrew/bin/python3
from account.contract_account import ContractAccount
from account.spot_account import SpotAccount
from snapshot_list import Snapshot, SnapshotList
from tools.tradingview_csv import load

if __name__ == '__main__':
  df = load('BINANCE_BTCUSDT, 120_cd3a1')
  print('你好，世界')
  print(df)
