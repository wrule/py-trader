
from typing import List
from numba.experimental import jitclass
from numba_try.kline import KLine

@jitclass
class History:
  def __init__(
    self,
    klines: List[KLine],
  ):
    self.klines = klines
    self.lastIndex = 0
  
  klines: List[KLine]
  lastIndex: int
  
  def length(self):
    return self.lastIndex + 1
  
  def reverse(self, index: int):
    return self.klines[self.lastIndex - index]
  
  def last(self):
    return self.reverse(0)
  
  def prev(self):
    return self.reverse(1)

    
