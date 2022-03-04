
from numba.experimental import jitclass
from numba_try.strategy import Strategy
from numba_try.trader import Trader

@jitclass
class Two(Strategy):
  def __init__(
    self,
    trader: Trader,
  ):
    super().__init__(trader)

  def show():
    print(1234)
