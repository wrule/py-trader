from datetime import datetime
from numba.experimental import jitclass

@jitclass
class KLine:
  def __init__(
    self,
    time: datetime,
    open: float,
    high: float,
    low: float,
    close: float,
    volume: float,
    closed: bool,
  ):
    self.time = time
    self.open = open
    self.high = high
    self.low = low
    self.close = close
    self.volume = volume
    self.closed = closed

  time: datetime
  open: float
  high: float
  low: float
  close: float
  volume: float
  closed: bool
