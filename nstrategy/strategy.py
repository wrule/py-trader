from typing import List
from numba import int64
from numba.experimental import jitclass
from numba.typed import List as NBList

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


