
from kline import KLine


class Trader:
  def __init__(
    self,
    funds: float = 100,
    assets: float = 0,
    buyFee: float = 0.02,
    sellFee: float = 0.02,
  ):
    self.funds = funds
    self.assets = assets
    self.buyFee = buyFee
    self.sellFee = sellFee
  
  funds: float = 0
  fundsDebt: float = 0
  assets: float = 0
  assetsDebt: float = 0
  buyFee: float = 0
  sellFee: float = 0
  
  def start(self):
    pass
  
  def end(self):
    pass
  
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
  
  def long(
    self,
    kline: KLine,
  ):
    pass

  def short(
    self,
    kline: KLine,
  ):
    pass