
import datetime
import pandas as pd
from pandas import DataFrame
from strategy.strategy import Strategy
from trader import Trader

class TwoLinesCrossX(Strategy):
  def __init__(
    self,
    trader: Trader,
    fast: str,
    slow: str,
  ):
    super().__init__(trader)
    self.fast = fast
    self.slow = slow
  
  fast: str
  slow: str
  
  def ready(self):
    return (
      self.length() >= 2 and
      self.twoLinesReady()
    )
    
  def twoLinesReady(self):
    return (
      not pd.isnull(self.lastFast()) and
      not pd.isnull(self.lastSlow()) and
      not pd.isnull(self.prevFast()) and
      not pd.isnull(self.prevSlow())
    )
  
  def lastFast(self):
    return self.last(self.fast)
  
  def lastSlow(self):
    return self.last(self.slow)
  
  def prevFast(self):
    return self.prev(self.fast)
  
  def prevSlow(self):
    return self.prev(self.slow)
  
  position = 1
  
  def lastIsWin(self):
    if self.trader.transactionList.length() >= 1:
      return self.trader.transactionList.last().win()
    return True

  def watch(self):
    if (
      self.prevFast() <= self.prevSlow() and
      self.lastFast() > self.lastSlow()
    ):
      self.trader.start(self.last('Date'), self.last('Close'))
      self.trader.buy(self.lastRecord(), self.position)
    elif (
      self.prevFast() >= self.prevSlow() and
      self.lastFast() < self.lastSlow()
    ):
      self.trader.sell(self.lastRecord(), 1)
      self.trader.end(self.last('Date'), self.last('Close'))
      if self.lastIsWin():
        self.position *= 1
      else:
        self.position *= 1
