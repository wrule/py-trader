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
  
  def snapshot(
    self,
    kline: KLine,
  ):
    return Snapshot(
      kline.time,
      self.funds,
      self.fundsDebt,
      self.assets,
      self.assetsDebt,
      kline.close,
    )
  
  def start(
    self,
    kline: KLine,
  ):
    self.transactionList.start(self.snapshot(kline))
  
  def end(
    self,
    kline: KLine,
  ):
    self.transactionList.end(self.snapshot(kline))
    
  def record(
    self,
    kline: KLine,
  ):
    self.snapshotList.append(self.snapshot(kline))
  
  def buy(
    self,
    kline: KLine,
    percent: int = 1,
  ):
    if (
      self.funds > 0 and
      percent > 0 and
      percent <= 1 and
      kline.close > 0
    ):
      useFunds = self.funds * percent
      self.funds -= useFunds
      self.assets += (useFunds / kline.close) * (1 - self.buyFee)
      return True
    return False
  
  def sell(
    self,
    kline: KLine,
    percent: int = 1,
  ):
    if (
      self.assets > 0 and
      percent > 0 and
      percent <= 1 and
      kline.close >= 0
    ):
      useAssets = self.assets * percent
      self.assets -= useAssets
      self.funds += (useAssets * kline.close) * (1 - self.sellFee)
      return True
    return False
