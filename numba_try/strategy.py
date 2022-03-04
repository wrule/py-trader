from typing import List
from numba import int64
from numba.experimental import jitclass
from dataclasses import dataclass
from numba.typed import List as NBList
from numba_try.kline import KLine
from numba_try.trader import Trader
from abc import ABC, abstractmethod

class Strategy:
  trader: Trader
  lastIndex: int
  hist: List[KLine]

  def __init__(
    self,
    trader: Trader,
  ):
    self.trader = trader
    self.lastIndex = 0
    
  def Backtesting(
    self,
    hist: List[KLine],
  ):
    self.hist = hist
    self.trader.reset()
    for index in range(len(hist)):
      self.lastIndex = index
      # if self.ready():
      #   self.watch()


