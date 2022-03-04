from typing import List
from numba import int64
from numba.experimental import jitclass
from dataclasses import dataclass
from numba.typed import List as NBList
from numba_try.kline import KLine
from numba_try.trader import Trader

@jitclass
class Strategy:
  lastIndex: int
  hist: List[int]
  trader: Trader

  def __init__(
    self,
    trader: Trader,
  ):
    self.lastIndex = 0
    self.hist = NBList([1])
    self.trader = trader
    
  def show(self):
    k = KLine(0, 0, 0, 0, 0, 0, False)
    print(self.hist)


