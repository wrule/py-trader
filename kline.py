from dataclasses import dataclass
import datetime

@dataclass
class KLine:
  time: datetime
  open: float
  high: float
  low: float
  close: float
  volume: float
  closed: bool
