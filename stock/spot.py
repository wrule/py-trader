from typing import Any, Dict
from stock.stock import Stock

class Spot(Stock):
  def __init__(
    self,
    volume: float,
    data: Dict[str, Any],
  ):
    super().__init__(volume, data)
  
  def start_valuation(self) -> float:
    return self.volume * self.restockPrice
  
  def current_valuation(self, data: Dict[str, Any]) -> float:
    return self.volume * data['Close']
