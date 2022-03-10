from typing import Any, Dict
from stock.stock import Stock

class Short(Stock):
  def __init__(
    self,
    volume: float,
    data: Dict[str, Any],
    lever: int,
  ):
    super().__init__(volume, data)
    self.lever = lever
    
  lever: int
  
  def start_valuation(self) -> float:
    return self.volume * self.price
  
  def current_valuation(self, data: Dict[str, Any]) -> float:
    return self.volume * data['Close']
  
  def profit(self, data: Dict[str, Any]):
    return self.start_valuation() - self.current_valuation(data)
