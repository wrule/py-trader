from strategy.strategy import Strategy
from trader import Trader
import math

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
      not math.isnan(self.prev()[self.fast]) and
      not math.isnan(self.prev()[self.slow]) and
      not math.isnan(self.last()[self.fast]) and
      not math.isnan(self.last()[self.slow])
    )

  def watch(self):
    if (
      self.prev()[self.fast] <= self.prev()[self.slow] and
      self.last()[self.fast] > self.last()[self.slow]
    ):
      self.trader.start(self.last())
      self.trader.buy(self.last(), 1)
    elif (
      self.prev()[self.fast] >= self.prev()[self.slow] and
      self.last()[self.fast] < self.last()[self.slow]
    ):
      self.trader.sell(self.last(), 1)
      self.trader.end(self.last())
