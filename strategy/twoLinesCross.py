
import datetime
import pandas as pd
from pandas import DataFrame
from strategy.strategy import Strategy
from trader import Trader

class TwoLinesCross(Strategy):
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

  def watch(self):
    if (
      self.prevFast() <= self.prevSlow() and
      self.lastFast() > self.lastSlow()
    ):
      self.trader.buy(self.lastRecord(), 1)
    elif (
      self.prevFast() >= self.prevSlow() and
      self.lastFast() < self.lastSlow()
    ):
      self.trader.sell(self.lastRecord(), 1)
