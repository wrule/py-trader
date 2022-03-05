from dataclasses import dataclass
import datetime
from typing import Any, Dict

@dataclass
class KLine:
  time: datetime
  open: float
  high: float
  low: float
  close: float
  volume: float
  closed: bool
  data: Dict[str, Any]
