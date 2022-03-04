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
  
  def test(
    self,
    hist: History,
  ):
    for lastIndex in range(len(hist.klines)):
      hist.lastIndex = lastIndex
      print(hist.length())
