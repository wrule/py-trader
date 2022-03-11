import datetime
from typing import Any, Dict
from stock.stock import Stock

class Short(Stock):
  def __init__(
    self,
    volume: float,
    price: float,
    date: datetime,
    lever: int,
    direction: int = 1,
  ):
    super().__init__(volume, price, date, direction)
    self.lever = lever
    
  lever: int

  def deposit(self, price: float):
    return self.current_valuation(price) / self.lever
