from datetime import datetime
from typing import Any, Dict

class Stock:
  def __init__(
    self,
    volume: float,
    price: float,
    date: datetime,
    direction: int = 1,
  ):
    self.volume = volume
    self.price = price
    self.date = date
    self.direction = direction
  
  volume: float
  price: float
  date: datetime
  direction: int

  def start_valuation(self) -> float:
    return self.volume * self.price

  def current_valuation(self, price: float) -> float:
    return self.volume * price

  def profit(self, price: float):
    return self.direction * (self.current_valuation(price) - self.start_valuation())

  def profitable(self, price: float):
    return self.profit(price) > 0
