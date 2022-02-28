
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
      
      startTime = self.start.datetime,
      startFunds = self.start.funds,
      startAssets = self.start.assets,
      startFundsDebt = self.start.fundsDebt,
      startAssetsDebt = self.start.assetsDebt,
      startPrice = self.start.price,
      startAssetsValuation = self.start.assetsValuation(),
      startDebtValuation = self.start.debtValuation(),
      startValuation = self.start.valuation(),
      
      endTime = self.end.datetime,
      endFunds = self.end.funds,
      endAssets = self.end.assets,
      endFundsDebt = self.end.fundsDebt,
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
  startAssets: float
  startFundsDebt: float
  startAssetsDebt: float
  startPrice: float
  startAssetsValuation: float
  startDebtValuation: float
  startValuation: float
  
  endTime: datetime
  endFunds: float
  endAssets: float
  endFundsDebt: float
  endAssetsDebt: float
  endPrice: float
  endAssetsValuation: float
  endDebtValuation: float
  endValuation: float

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

