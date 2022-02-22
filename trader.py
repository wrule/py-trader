
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
  
  def buy(
    self,
    kline: KLine,
    position: int = 1,
  ):
    if self.funds > 0 and position > 0 and kline.close > 0:
      useFunds = self.funds * position
      self.funds -= useFunds
      self.assets += useFunds / kline.close * (1 - self.buyFee)
      return True
    return False
      
  
  def sell(
    self,
    kline: KLine,
    position: int = 1,
  ):
    pass
  
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