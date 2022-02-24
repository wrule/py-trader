import time
from pandas import DataFrame, Series

from abc import ABC, abstractmethod

from trader import Trader

class Strategy(ABC):
  def __init__(
    self,
    trader: Trader,
  ):
    self.trader = trader
  
  trader: Trader = None
  hist: DataFrame = None
  
  def length(
    self,
  ):
    return len(self.hist.index)
  
  def row(
    self,
    index: int,
  ):
    return self.hist.iloc[index]
    
  def prev(
    self,
    field: str,
  ):
    return self.hist.tail(2)[field].iloc[0]
  
  def last(
    self,
    field: str,
  ):
    return self.hist.tail(2)[field].iloc[1]
  
  @abstractmethod
  def watch(
    self,
    hist: DataFrame,
  ):
    pass

  @abstractmethod
  def ready(
    self,
    hist: DataFrame,
  ):
    return False
  
  def Backtesting(
    self,
    hist: DataFrame,
  ):
    for index in range(len(hist.index)):
      self.hist = hist.iloc[0 : index + 1]
      if self.ready(hist):
        self.watch(self.hist)
        time.sleep(0.5)
