
from dataclasses import dataclass
from datetime import datetime
from typing import List

from pandas import DataFrame
from snapshot_list import Snapshot

@dataclass
class Transaction:
  start: datetime
  end: datetime
  startFunds: float = 0
  startAssets: float = 0
  startFundsDebt: float = 0
  startAssetsDebt: float = 0
  startPrice: float = 0
  endFunds: float = 0
  endAssets: float = 0
  endFundsDebt: float = 0
  endAssetsDebt: float = 0
  endPrice: float = 0

class TransactionList:
  list: List[Transaction] = []
  txn = Transaction(0, 0)
  started = False
  
  def start(self, snapshot: Snapshot):
    if self.started == False:
      self.txn.start = snapshot.datetime
      self.txn.startFunds = snapshot.funds
      self.txn.startFundsDebt = snapshot.fundsDebt
      self.txn.startAssets = snapshot.assets
      self.txn.startAssetsDebt = snapshot.assetsDebt
      self.txn.startPrice = snapshot.price
      self.started = True
  
  def end(self, snapshot: Snapshot):
    if self.started == True:
      self.txn.end = snapshot.datetime
      self.txn.endFunds = snapshot.funds
      self.txn.endFundsDebt = snapshot.fundsDebt
      self.txn.endAssets = snapshot.assets
      self.txn.endAssetsDebt = snapshot.assetsDebt
      self.txn.endPrice = snapshot.price
      self.list.append(self.txn)
      self.txn = Transaction(0, 0)
      self.started = False
      
  def dataframe(self):
    df = DataFrame(self.list)
    df['startAssetValuation'] = df.apply(lambda row: row['startFunds'] + row['startAssets'] * row['startPrice'], axis = 1)
    df['startDebtValuation'] = df.apply(lambda row: row['startFundsDebt'] + row['startAssetsDebt'] * row['startPrice'], axis = 1)
    df['startValuation'] = df.apply(lambda row: row['startAssetValuation'] - row['startDebtValuation'], axis = 1)
    df['endAssetValuation'] = df.apply(lambda row: row['endFunds'] + row['endAssets'] * row['endPrice'], axis = 1)
    df['endDebtValuation'] = df.apply(lambda row: row['endFundsDebt'] + row['endAssetsDebt'] * row['endPrice'], axis = 1)
    df['endValuation'] = df.apply(lambda row: row['endAssetValuation'] - row['endDebtValuation'], axis = 1)
    return df

