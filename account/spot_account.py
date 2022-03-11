from datetime import datetime
from typing import List
from stock.spot import Spot

class SpotAccount:
  def __init__(
    self,
    funds: float,
    buyFee: float,
    sellFee: float,
  ):
    self.funds = funds
    self.buyFee = buyFee
    self.sellFee = sellFee
    self.spotList = []

  funds: float
  buyFee: float
  sellFee: float
  spotList: List[Spot]
  
  def buy_funds(
    self,
    use_funds: float,
    price: float,
    date: datetime,
  ):
    if use_funds <= self.funds and price > 0:
      self.funds -= use_funds
      buy_assets = (use_funds / price) * (1 - self.buyFee)
      spot = Spot(buy_assets, price, date)
      self.spotList.append(spot)
      return True
    return False
  
  def buy_assets(
    self,
    use_assets: float,
    price: float,
    date: datetime,
  ):
    if use_assets > 0:
      use_funds = use_assets * price / (1 - self.buyFee)
      return self.buy_funds(use_funds, price, date)
    return False
  
  def buy_funds_percent(
    self,
    percent: float,
    price: float,
    date: datetime,
  ):
    if percent > 0 and percent <= 1:
      use_funds = self.funds * percent
      return self.buy_funds(use_funds, price, date)
    return False
  
  def sell(self):
    pass

      