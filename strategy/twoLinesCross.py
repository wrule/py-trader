
import pandas as pd
from pandas import DataFrame
from strategy.strategy import Strategy

class TwoLinesCross(Strategy):
  def __init__(
    self,
    fast: str,
    slow: str,
  ):
    self.fast = fast
    self.slow = slow
  
  fast: str = ''
  slow: str = ''
  
  def ready(self, hist: DataFrame):
    return (
      self.length() >= 2 and
      self.twoLinesReady(hist)
    )
    
  def twoLinesReady(self, hist: DataFrame):
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

  def watch(
    self,
    hist: DataFrame,
  ):
    print(self.length(), self.last(self.fast), self.last(self.slow))
    if (
      self.prevFast() <= self.prevSlow() and
      self.lastFast() > self.lastSlow()
    ):
      print('买入')
    elif (
      self.prevFast() >= self.prevSlow() and
      self.lastFast() < self.lastSlow()
    ):
      print('卖出')
    else:
      print('无操作')