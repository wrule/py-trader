from typing import List
from numba import int64
from numba.experimental import jitclass
from dataclasses import dataclass
from numba.typed import List as NBList


@jitclass
@dataclass
class KLine:
  time: int
  open: float
  close: float
  high: float
  low: float
  volume: float
  closed: bool
  
  # def __init__(
  #   self,
  #   time: int,
  #   open: float,
  #   close: float,
  #   high: float,
  #   low: float,
  #   volume: float,
  #   closed: bool,
  # ):
  #   self.time = time
  #   self.open = open
  #   self.close = close
  #   self.high = high
  #   self.low = low
  #   self.volume = volume
  #   self.closed = closed

@jitclass
class Strategy:
  lastIndex: int
  hist: List[int]

  def __init__(self):
    pass
    # self.lastIndex = 0
    # self.hist = NBList([1])
    
  def show(self):
    print(self.hist)


