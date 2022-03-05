import time
from numba.experimental import jitclass
from numba_try.trader import Trader
from numba_try.history import History

@jitclass
class Backtester:
  def __init__(
    self,
    trader: Trader,
  ):
    self.trader = trader
  
  trader: Trader
  
  def test2(
    self,
    hist: History, 
  ):
    result = 0
    for y in range(20100):
      result = result + self.test(hist)
    return result
  
  def test(
    self,
    hist: History,
  ):
    result = 0
    for lastIndex in range(len(hist.klines)):
      hist.lastIndex = lastIndex
      if (
        hist.prev().close <= hist.prev().open and
        hist.last().close > hist.prev().open
      ):
        result = result + hist.last().close
      if (
        hist.prev().close >= hist.prev().open and
        hist.last().close < hist.prev().open
      ):
        result = result + hist.last().open
    return result
