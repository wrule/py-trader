
from dataclasses import dataclass
from datetime import datetime
from typing import List
from pandas import DataFrame
from snapshot_list import Snapshot

class Transaction:
  start: Snapshot
  end: Snapshot
  
  def win(self):
    return self.end.valuation() > self.start.valuation()
  
  def profit(self):
    return self.end.valuation() - self.start.valuation()
  
  def profitRate(self):
    return self.profit() / self.start.valuation()
  
  def toData(self):
    return TransactionData(
      win = self.win(),
      profit = self.profit(),
      profitRate = self.profitRate(),
      
      startTime = self.start.time,
      startFunds = self.start.funds,
      startFundsDebt = self.start.fundsDebt,
      startAssets = self.start.assets,
      startAssetsDebt = self.start.assetsDebt,
      startPrice = self.start.price,
      startAssetsValuation = self.start.assetsValuation(),
      startDebtValuation = self.start.debtValuation(),
      startValuation = self.start.valuation(),
      
      endTime = self.end.time,
      endFunds = self.end.funds,
      endFundsDebt = self.end.fundsDebt,
      endAssets = self.end.assets,
      endAssetsDebt = self.end.assetsDebt,
      endPrice = self.end.price,
      endAssetsValuation = self.end.assetsValuation(),
      endDebtValuation = self.end.debtValuation(),
      endValuation = self.end.valuation(),
    )

@dataclass
class TransactionData:
  win: bool
  profit: float
  profitRate: float
  
  startTime: datetime
  startFunds: float
  startFundsDebt: float
  startAssets: float
  startAssetsDebt: float
  startPrice: float
  startAssetsValuation: float
  startDebtValuation: float
  startValuation: float
  
  endTime: datetime
  endFunds: float
  endFundsDebt: float
  endAssets: float
  endAssetsDebt: float
  endPrice: float
  endAssetsValuation: float
  endDebtValuation: float
  endValuation: float

class TransactionList:
  def __init__(self):
    self.list = []
  
  list: List[Transaction]
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
    return self.list[-index - 1]
  
  def length(self):
    return len(self.list)
  
  def dataframe(self):
    df = DataFrame([item.toData() for item in self.list])
    df.index = range(self.length())
    return df
