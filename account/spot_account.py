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
    self.assets = 0
    self.buyFee = buyFee
    self.sellFee = sellFee
    self.spotList = []

  funds: float
  assets: float
  buyFee: float
  sellFee: float
  spotList: List[Spot]
  
  def buy_funds(
    self,
    use_funds: float,
    price: float,
    date: datetime,
  ):
    if use_funds < 0 or price <= 0:
      return None
    use_funds = (
      use_funds
      if use_funds <= self.funds
      else self.funds
    )
    self.funds -= use_funds
    get_assets = use_funds / price * (1 - self.buyFee)
    spot = Spot(get_assets, price, date)
    self.spotList.append(spot)
    self.assets += get_assets
    return (use_funds, get_assets)
  
  def buy_assets(
    self,
    get_assets: float,
    price: float,
    date: datetime,
  ):
    return self.buy_funds(get_assets * price / (1 - self.buyFee), price, date)
  
  def buy_funds_percent(
    self,
    percent: float,
    price: float,
    date: datetime,
  ):
    return self.buy_funds(self.funds * percent, price, date)
  
  def sell_stock(
    self,
    index: int,
    use_assets: float,
    price: float,
    date: datetime,
  ):
    if use_assets < 0:
      return None
    use_assets = (
      use_assets
      if use_assets <= self.spotList[index].volume
      else self.spotList[index].volume
    )
    self.spotList[index].volume -= use_assets
    self.assets -= use_assets
    get_funds = use_assets * price * (1 - self.sellFee)
    self.funds += get_funds
    if self.spotList[index].volume <= 0:
      del self.spotList[index]
    return (use_assets, get_funds)
  
  def sell_stock_percent(
    self,
    index: int,
    percent: float,
    price: float,
    date: datetime,
  ):
    return self.sell_stock(
      index,
      self.spotList[index].volume * percent,
      price,
      date,
    )
  
  def sell_all(
    self,
    price: float,
    date: datetime,
  ):
    use_assets_total = 0
    get_funds_total = 0
    while len(self.spotList) > 0:
      (use_assets, get_funds) = self.sell_stock_percent(0, 1, price, date)
      use_assets_total += use_assets
      get_funds_total += get_funds
    return (use_assets_total, get_funds_total)
  
  def sell_assets(
    self,
    use_assets: float,
    price: float,
    date: datetime,
  ):
    use_assets_total = 0
    get_funds_total = 0
    while use_assets > 0 and len(self.spotList) > 0:
      (assets, funds) = self.sell_stock(0, use_assets, price, date)
      use_assets -= assets
      use_assets_total += assets
      get_funds_total += funds
    return (use_assets_total, get_funds_total)
  
  def sell_funds(
    self,
    get_funds: float,
    price: float,
    date: datetime,
  ):
    use_assets_total = 0
    get_funds_total = 0
    while get_funds > 0 and len(self.spotList) > 0:
      use_assets = get_funds / price / (1 - self.sellFee)
      (assets, funds) = self.sell_stock(0, use_assets, price, date)
      get_funds -= funds
      use_assets_total += assets
      get_funds_total += funds
    return (use_assets_total, get_funds_total)
  
  def sell_assets_percent(
    self,
    percent: float,
    price: float,
    date: datetime,
  ):
    return self.sell_assets(self.assets * percent, price, date)


      