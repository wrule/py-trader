
from dataclasses import dataclass
from datetime import datetime
from typing import List
from pandas import DataFrame
from snapshot_list import Snapshot

class Transaction:
  direction: int
  start: Snapshot
  end: Snapshot
  
  def win(self):
    return self.end.valuation > self.start.valuation
  
  def profit(self):
    return self.end.valuation - self.start.valuation
  
  def profitRate(self):
    return self.profit() / self.start.valuation
  
  def toData(self):
    return TransactionData(
      direction = self.direction,
      win = self.win(),
      profit = self.profit(),
      profitRate = self.profitRate(),
      startTime = self.start.time,
      startPrice = self.start.price,
      startValuation = self.start.valuation,
      endTime = self.end.time,
      endPrice = self.end.price,
      endValuation = self.end.valuation,
    )

@dataclass
class TransactionData:
  direction: int
  win: bool
  profit: float
  profitRate: float
  startTime: datetime
  startPrice: float
  startValuation: float
  endTime: datetime
  endPrice: float
  endValuation: float

class TransactionList:
  def __init__(self):
    self.list = []
  
  list: List[Transaction]
  txn = Transaction()
  started = False
  
  def start(self, snapshot: Snapshot, direction: int = 1):
    if self.started == False:
      self.txn.direction = direction
      self.txn.start = snapshot
      self.started = True
  
  def end(self, snapshot: Snapshot):
    if self.started == True:
      self.txn.end = snapshot
      self.list.append(self.txn)
      self.txn = Transaction()
      self.started = False
      
  def last(self, index: int = 0):
    return self.list[-index - 1]
  
  def length(self):
    return len(self.list)
  
  def dataframe(self):
    df = DataFrame([item.toData() for item in self.list])
    df.index = range(self.length())
    return df
