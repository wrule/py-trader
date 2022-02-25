
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
  
  bugFlag = False
  sellFlag = False

  def watch(self):
    if (
      self.prevFast() <= self.prevSlow() and
      self.lastFast() > self.lastSlow()
    ):
      self.trader.start(self.last('Date'), self.last('Close'))
      self.trader.buy(self.lastRecord(), 0)
      self.bugFlag = True
      return
      
    if self.bugFlag == True and self.last('Close') > self.prev('Close'):
      self.trader.buy(self.lastRecord(), 1)
      self.bugFlag = False
      return

    if (
      self.prevFast() >= self.prevSlow() and
      self.lastFast() < self.lastSlow()
    ):
      self.trader.sell(self.lastRecord(), 1)
      self.trader.end(self.last('Date'), self.last('Close'))
      self.sellFlag = True
      return
    
    if self.sellFlag == True and self.last('Close') < self.prev('Close'):
      self.trader.sell(self.lastRecord(), 1)
      self.sellFlag = False
      return
