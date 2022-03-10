from typing import Any, Dict

class Short:
  def __init__(
    self,
    volume: float,
    data: Dict[str, Any],
  ):
    super().__init__(volume, data)