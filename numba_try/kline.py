from numba.experimental import jitclass

@jitclass
class KLine:
  time: int
  open: float
  high: float
  low: float
  close: float
  volume: float
  closed: bool
  
  def __init__(
    self,
    time: int,
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
