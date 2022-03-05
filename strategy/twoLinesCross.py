
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
      self.hist.length() >= 2 and
      self.twoLinesReady()
    )
    
  def twoLinesReady(self):
    return (
      not pd.isnull(self.last().open) and
      not pd.isnull(self.last().close) and
      not pd.isnull(self.prev().open) and
      not pd.isnull(self.prev().close)
    )

  def watch(self):
    if (
      self.prev().close <= self.prev().open and
      self.last().close > self.last().open
    ):
      self.trader.start(self.last())
      self.trader.buy(self.last(), 1)
    elif (
      self.prev().close >= self.prev().open and
      self.last().close < self.last().open
    ):
      self.trader.sell(self.last(), 1)
      self.trader.end(self.last())
