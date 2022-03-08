from collections.abc import Callable
from typing import List, Tuple
from optimizer.int_space import IntPoint, IntSpace
from bisect import bisect

class Random:
  def __init__(
    self,
    space: IntSpace,
    batchSize: int,
  ):
    self.space = space
    self.batchSize = batchSize
    self.ranking = []
  
  space: IntSpace
  density: float
  batchSize: int
  ranking: List[Tuple[IntPoint, float]]
  
  def push(self, point: IntSpace, score: float):
    self.ranking.append((point, score))
    self.ranking.sort(key = lambda t: t[1], reverse = True)
    if len(self.ranking) > 10:
      del self.ranking[10]
    
  
  def explore(
    self,
    func: Callable[..., float],
  ):
    while True:
      for i in range(self.batchSize):
        point = self.space.random()
        score = func(**point)
        self.push(point, score)
      print([x[1] for x in self.ranking])

