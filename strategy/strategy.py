from typing import Any, Dict, List
from abc import ABC, abstractmethod
from trader import Trader

class Strategy(ABC):
  def __init__(
    self,
    trader: Trader,
  ):
    self.trader = trader
  
  trader: Trader = None
  hist: List[Dict[str, Any]] = []
  lastIndex = 0
  
  @abstractmethod
  def ready(self):
    return False
  
  @abstractmethod
  def watch(self):
    pass

  def length(self):
    return self.lastIndex + 1
  
  def index(self, index: int):
    assert index >= 0 and index <= self.lastIndex
    return self.lastIndex - index
  
  def record(self, index: int):
    return self.hist[self.index(index)]
  
  def lastRecord(self):
    return self.record(0)
  
  def prevRecord(self):
    return self.record(1)
  
  def last(self, field: str):
    return self.lastRecord()[field]
  
  def prev(self, field: str):
    return self.prevRecord()[field]
  
  def field(self, index: int, field: str):
    return self.record(index)[field]
  
  def lastHist(self):
    return self.hist[0 : self.length()]
  
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
