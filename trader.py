
from datetime import datetime
from typing import Any, Dict

from kline import KLine
from snapshot_list import Snapshot, SnapshotList
from transaction_list import TransactionList

class Trader:
  def __init__(
    self,
    funds: float = 100,
    buyFee: float = 0.001,
    sellFee: float = 0.001,
  ):
    self.initFunds = funds
    self.buyFee = buyFee
    self.sellFee = sellFee
    self.reset()
  
  initFunds: float
  funds: float
  fundsDebt: float
  assets: float
  assetsDebt: float
  buyFee: float
  sellFee: float
  snapshotList: SnapshotList
  transactionList: TransactionList
  
  def reset(self):
    self.funds = self.initFunds
    self.fundsDebt = 0
    self.assets = 0
    self.assetsDebt = 0
    self.snapshotList = SnapshotList()
    self.transactionList = TransactionList()
  
  def makeSnapshot(
    self,
    datetime: datetime,
    price: float,
  ):
    return Snapshot(
      datetime,
      self.funds,
      self.assets,
      self.fundsDebt,
      self.assetsDebt,
      price,
    )
  
  def start(
    self,
    datetime: datetime,
    price: float,
  ):
    self.transactionList.start(self.makeSnapshot(datetime, price))
  
  def end(
    self,
    datetime: datetime,
    price: float,
  ):
    self.transactionList.end(self.makeSnapshot(datetime, price))
    
  def log(
    self,
    datetime: datetime,
    price: float,
  ):
    self.snapshotList.append(self.makeSnapshot(datetime, price))
  
  def buy(
    self,
    kline: Dict[str, Any],
    percent: int = 1,
  ):
    if (
      self.funds > 0 and
      percent > 0 and
      percent <= 1 and
      kline['Close'] > 0
    ):
      useFunds = self.funds * percent
      self.funds -= useFunds
      self.assets += (useFunds / kline['Close']) * (1 - self.buyFee)
      return True
    return False
  
  def sell(
    self,
    kline: Dict[str, Any],
    percent: int = 1,
  ):
    if (
      self.assets > 0 and
      percent > 0 and
      percent <= 1 and
      kline['Close'] >= 0
    ):
      useAssets = self.assets * percent
      self.assets -= useAssets
      self.funds += (useAssets * kline['Close']) * (1 - self.sellFee)
      return True
    return False
