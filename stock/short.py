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
    return 0
  
  def current_valuation(self, data: Dict[str, Any]) -> float:
    return 0
