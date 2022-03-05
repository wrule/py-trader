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
    lastIndex = 0
    for y in range(20100):
      for x in range(2724):
        lastIndex = x * y
