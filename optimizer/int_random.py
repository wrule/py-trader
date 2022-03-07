from typing import Callable
from int_space import IntSpace

class Random:
  def __init__(
    self,
    space: IntSpace,
  ):
    pass
  
  def explore(
    self,
    func: Callable([], float),
  ):
    a = func()
    pass