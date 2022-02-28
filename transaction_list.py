
from dataclasses import dataclass
from datetime import datetime
from typing import List

from pandas import DataFrame
from snapshot_list import Snapshot

class Transaction:
  start: Snapshot = None
  end: Snapshot = None
  
  def win(self):
    return self.end.valuation() > self.start.valuation()
  
  def profit(self):
    return self.end.valuation() - self.start.valuation()
  
  def profitRate(self):
    return self.profit() / self.start.valuation()

@dataclass
class TransactionX:
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
  txn = Transaction()
  started = False
  
  def start(self, snapshot: Snapshot):
    if self.started == False:
      self.txn.start = snapshot
      self.started = True
  
  def end(self, snapshot: Snapshot):
    if self.started == True:
      self.txn.end = snapshot
      self.list.append(self.txn)
      self.txn = Transaction()
      self.started = False
      
  def last(self, index: int = 0):
    return self.list[-1]
  
  def dataframe(self):
    pass

