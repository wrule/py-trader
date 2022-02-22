from dataclasses import dataclass

@dataclass
class KLine:
  time: int
  open: float
  close: float
  high: float
  low: float
  volume: float
  closed: bool
