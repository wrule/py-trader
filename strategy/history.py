from typing import List
from kline import KLine

class History:
  def __init__(
    self,
    klines: List[KLine],
  ):
    self.klines = klines
    self.lastIndex = 0
  
  klines: List[KLine]
  lastIndex: int
  
  def last(self, index: int = 0):
    return self.klines[self.lastIndex - index]

  def prev(self):
    return self.last(1)
