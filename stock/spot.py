from typing import Any, Dict
from stock.stock import Stock

class Spot(Stock):
  def __init__(
    self,
    volume: float,
    data: Dict[str, Any],
  ):
    super().__init__(volume, data)
