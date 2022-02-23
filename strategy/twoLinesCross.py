
from pandas import DataFrame
from strategy.strategy import Strategy

class TwoLinesCross(Strategy):
  def __init__(self):
    pass

  def watch(
    self,
    hist: DataFrame,
  ):
    print(self.length())
