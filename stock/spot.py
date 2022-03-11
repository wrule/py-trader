from datetime import datetime
from stock.stock import Stock

class Spot(Stock):
  def __init__(
    self,
    volume: float,
    price: float,
    date: datetime,
  ):
    super().__init__(volume, price, date, 1)
