# from typing import Callable
from collections.abc import Callable
from typing import List, Tuple
from optimizer.int_space import IntPoint, IntSpace

class Random:
  def __init__(
    self,
    space: IntSpace,
  ):
    self.space = space
    self.ranking = []
  
  space: IntSpace
  ranking: List[Tuple[IntPoint, float]]
  
  def push(self, point: IntSpace, score: float):
    pass
  
  def explore(
    self,
    func: Callable[..., float],
  ):
    while True:
      args = self.space.random()
      result = func(**args)
      print(args, result)
