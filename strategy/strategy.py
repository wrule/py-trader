from typing import Any, Dict, List
from abc import ABC, abstractmethod
from kline import KLine
from trader import Trader

class Strategy(ABC):
  def __init__(
    self,
    trader: Trader,
  ):
    self.trader = trader
  
  trader: Trader
  hist: List[KLine]
  lastIndex = 0
  
  @abstractmethod
  def ready(self):
    return False
  
  @abstractmethod
  def watch(self):
    pass

  def length(self):
    return self.lastIndex + 1
  
  def reverse(self, index: int = 0):
    return self.hist[-index - 1]

  def Backtesting(
    self,
    hist: List[Dict[str, Any]],
  ):
    self.hist = hist
    for index in range(len(hist)):
      self.lastIndex = index
      if self.ready():
        self.watch()
      self.trader.log(self.last('Date'), self.last('Close'))
