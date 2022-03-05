
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
    return self.hist.length() >= 44

  def watch(self):
    if (
      self.prev().data[self.fast] <= self.prev().data[self.slow] and
      self.last().data[self.fast] > self.last().data[self.slow]
    ):
      self.trader.start(self.last())
      self.trader.buy(self.last(), 1)
    elif (
      self.prev().data[self.fast] >= self.prev().data[self.slow] and
      self.last().data[self.fast] < self.last().data[self.slow]
    ):
      self.trader.sell(self.last(), 1)
      self.trader.end(self.last())
