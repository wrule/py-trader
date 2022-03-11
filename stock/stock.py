from datetime import datetime
from abc import ABC, abstractmethod
from typing import Any, Dict

class Stock(ABC):
  def __init__(
    self,
    volume: float,
    data: Dict[str, Any],
  ):
    self.volume = volume
    self.price = data['Close']
    self.date = data['Date']
  
  volume: float
  price: float
  date: datetime

  def start_valuation(self) -> float:
    return self.volume * self.price

  def current_valuation(self, data: Dict[str, Any]) -> float:
    return self.volume * data['Close']

  def profit(self, data: Dict[str, Any]):
    return self.current_valuation(data) - self.start_valuation()

  def profitable(self, data: Dict[str, Any]):
    return self.profit(data) > 0
