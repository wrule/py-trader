
import datetime
import pandas as pd
from pandas import DataFrame
from strategy.strategy import Strategy
from trader import Trader

class ThreeLinesCross(Strategy):
  def __init__(
    self,
    trader: Trader,
    fast: str,
    medium: str,
    slow: str,
  ):
    super().__init__(trader)
    self.fast = fast
    self.slow = slow
    self.medium = medium
  
  fast: str
  medium: str
  slow: str
  
  def ready(self):
    return (
      self.length() >= 2 and
      self.threeLinesReady()
    )
    
  def threeLinesReady(self):
    return (
      not pd.isnull(self.lastFast()) and
      not pd.isnull(self.lastMedium()) and
      not pd.isnull(self.lastSlow()) and
      not pd.isnull(self.prevFast()) and
      not pd.isnull(self.prevMedium()) and
      not pd.isnull(self.prevSlow())
    )
  
  def lastFast(self):
    return self.last(self.fast)
  
  def lastMedium(self):
    return self.last(self.medium)
  
  def lastSlow(self):
    return self.last(self.slow)
  
  def prevFast(self):
    return self.prev(self.fast)
  
  def prevMedium(self):
    return self.prev(self.medium)
  
  def prevSlow(self):
    return self.prev(self.slow)

  def watch(self):
    if (
      self.prevFast() <= self.prevSlow() and
      self.lastFast() > self.lastSlow()
    ):
      self.trader.start(self.last('Date'), self.last('Close'))
      self.trader.buy(self.lastRecord(), 1)
    elif (
      self.prevFast() >= self.prevSlow() and
      self.lastFast() < self.lastSlow()
    ):
      self.trader.sell(self.lastRecord(), 1)
      self.trader.end(self.last('Date'), self.last('Close'))
