from datetime import datetime
from stock.stock import Stock

class Contract(Stock):
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
