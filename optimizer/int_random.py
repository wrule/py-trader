# from typing import Callable
from collections.abc import Callable
from optimizer.int_space import IntSpace

class Random:
  def __init__(
    self,
    space: IntSpace,
  ):
    self.space = space
  
  space: IntSpace
  
  def explore(
    self,
    func,
  ):
    while True:
      args = self.space.random()
      result = func(**args)
      print(args, result)
