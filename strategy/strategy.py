import time
from typing import Any, Dict, List
from pandas import DataFrame, Series

from abc import ABC, abstractmethod

from trader import Trader

class Strategy(ABC):
  def __init__(
    self,
    trader: Trader,
  ):
    self.trader = trader
  
  trader: Trader = None
  
  @abstractmethod
  def watch(
    self,
    hist: DataFrame,
  ):
    pass

  @abstractmethod
  def ready(
    self,
    hist: DataFrame,
  ):
    return False
  
  hist: List[Dict[str, Any]] = []
  lastIndex = 0

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
    for index in range(len(hist)):
      self.lastIndex = index
      if self.ready(hist):
        self.watch(self.hist)

