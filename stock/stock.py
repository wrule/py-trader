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

  @abstractmethod
  def start_valuation(self) -> float:
    pass

  @abstractmethod
  def current_valuation(self, data: Dict[str, Any]) -> float:
    pass

  def profit(self, data: Dict[str, Any]):
    return self.current_valuation(data) - self.start_valuation()
  
  def profitable(self, data: Dict[str, Any]):
    return self.profit(data) > 0
