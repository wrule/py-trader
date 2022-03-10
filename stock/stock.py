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
    self.restockTime = data['Date']
    self.restockPrice = data['Close']
  
  volume: float
  restockTime: datetime
  restockPrice: float

  @abstractmethod
  def start_valuation(self) -> float:
    pass

  @abstractmethod
  def current_valuation(self, data: Dict[str, Any]) -> float:
    pass

  def profit(self):
    return self.current_valuation() - self.start_valuation()