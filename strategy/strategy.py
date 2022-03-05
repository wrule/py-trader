from typing import Any, Dict, List
from abc import ABC, abstractmethod
from kline import KLine
from trader import Trader
from strategy.history import History

class Strategy(ABC):
  def __init__(self, trader: Trader):
    self.trader = trader
  
  trader: Trader
  hist: History
  
  @abstractmethod
  def ready(self):
    return False
  
  @abstractmethod
  def watch(self):
    pass
  
  def last(self, index: int = 0):
    return self.hist.last(index)

  def prev(self):
    return self.hist.prev()

  def backtesting(self, hist: History):
    self.hist = hist
    self.trader.reset()
    for index in range(hist.length()):
      self.hist.lastIndex = index
      if self.ready():
        self.watch()
      self.trader.record(self.hist.last())
