import datetime
from typing import Any, Dict
from stock.stock import Stock

class Spot(Stock):
  def __init__(
    self,
    volume: float,
    price: float,
    date: datetime,
    direction: int = 1,
  ):
    super().__init__(volume, price, date, direction)
