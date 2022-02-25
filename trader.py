
from datetime import datetime
from typing import Any, Dict

from kline import KLine
from snapshot_list import Snapshot, SnapshotList
from transaction_list import TransactionList


class Trader:
  def __init__(
    self,
    funds: float = 100,
    assets: float = 0,
    buyFee: float = 0.002,
    sellFee: float = 0.002,
    transaction: bool = True,
    snapshot: bool = False,
  ):
    self.funds = funds
    self.assets = assets
    self.buyFee = buyFee
    self.sellFee = sellFee
    self.snapshot = snapshot
    self.transaction = transaction
  
  funds: float = 0
  fundsDebt: float = 0
  assets: float = 0
  assetsDebt: float = 0
  buyFee: float = 0
  sellFee: float = 0
  
  snapshot: bool = False
  snapshotList = SnapshotList()
  transaction: bool = True
  transactionList = TransactionList()
  
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
    if self.transaction:
      self.transactionList.start(self.makeSnapshot(datetime, price))
  
  def end(
    self,
    datetime: datetime,
    price: float,
  ):
    if self.transaction:
      self.transactionList.end(self.makeSnapshot(datetime, price))
    
  def log(
    self,
    datetime: datetime,
    price: float,
  ):
    if self.snapshot:
      self.snapshotList.append(self.snapshot(datetime, price))
  
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
  
  def long(
    self,
    kline: Dict[str, Any],
  ):
    pass

  def short(
    self,
    kline: Dict[str, Any],
  ):
    pass