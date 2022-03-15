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
      self.trader.spot.buy_funds_percent(1, self.last()['Close'], self.last()['Date'])
    elif (
      self.prev()[self.fast] >= self.prev()[self.slow] and
      self.last()[self.fast] < self.last()[self.slow]
    ):
      self.trader.spot.sell_all(self.last()['Close'], self.last()['Date'])

