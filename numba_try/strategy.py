from typing import List
from numba import int64
from numba.experimental import jitclass
from dataclasses import dataclass
from numba.typed import List as NBList
from numba_try.kline import KLine

@jitclass
class Strategy:
  lastIndex: int
  hist: List[int]

  def __init__(self):
    self.lastIndex = 0
    self.hist = NBList([1])
    
  def show(self):
    k = KLine(0, 0, 0, 0, 0, 0, False)
    print(self.hist)


