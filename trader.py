from typing import Any, Dict
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
  buyFee: float
  sellFee: float

  funds: float
  fundsDebt: float
  assets: float
  assetsDebt: float
  snapshotList: SnapshotList
  transactionList: TransactionList
  
  def reset(self):
    self.funds = self.initFunds
    self.fundsDebt = 0
    self.assets = 0
    self.assetsDebt = 0
    self.snapshotList = SnapshotList()
    self.transactionList = TransactionList()
  
  def snapshot(self, data: Dict[str, Any]):
    return Snapshot(
      data['Date'],
      self.funds,
      self.fundsDebt,
      self.assets,
      self.assetsDebt,
      data['Close'],
    )

  def buy_funds(self, data: Dict[str, Any], useFunds: float):
    if useFunds <= self.funds and data['Close'] > 0:
      self.funds -= useFunds
      self.assets += (useFunds / data['Close']) * (1 - self.buyFee)
      return True
    return False
  
  def buy_funds_percent(self, data: Dict[str, Any], percent: float):
    if percent > 0 and percent <= 1:
      useFunds = self.funds * percent
      return self.buy_funds(data, useFunds)
    return False

  def start(self, data: Dict[str, Any]):
    self.transactionList.start(self.snapshot(data))
  
  def end(self, data: Dict[str, Any]):
    self.transactionList.end(self.snapshot(data))
    
  def record(self, data: Dict[str, Any]):
    self.snapshotList.append(self.snapshot(data))
  
  def buy(
    self,
    data: Dict[str, Any],
    percent: int = 1,
  ):
    if (
      self.funds > 0 and
      percent > 0 and
      percent <= 1 and
      data['Close'] > 0
    ):
      useFunds = self.funds * percent
      self.funds -= useFunds
      self.assets += (useFunds / data['Close']) * (1 - self.buyFee)
      return True
    return False
  
  def sell(
    self,
    data: Dict[str, Any],
    percent: int = 1,
  ):
    if (
      self.assets > 0 and
      percent > 0 and
      percent <= 1 and
      data['Close'] >= 0
    ):
      useAssets = self.assets * percent
      self.assets -= useAssets
      self.funds += (useAssets * data['Close']) * (1 - self.sellFee)
      return True
    return False
