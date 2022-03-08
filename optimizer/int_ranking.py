
from typing import List, Tuple
from optimizer.int_space import IntPoint

Record = Tuple[IntPoint, float, bool]

class IntRanking:
  def __init__(
    self,
    limitSize: int = 10,
    enableSize: int = 3,
  ):
    self.limitSize = limitSize
    self.enableSize = enableSize
    self.ranking = []
  
  limitSize: int
  enableSize: int
  ranking: List[Record]
  
  def first(self):
    return self.ranking[0]
  
  def last(self):
    return self.ranking[-1]
  
  def try_push(self, point: IntPoint, score: int):
    if (
      len(self.ranking) < self.limitSize or
      score > self.last()[1]
    ):
      index = 0
      for item in self.ranking:
        if score > item[1]:
          break
        index += 1
      self.ranking.insert(index, (point, score, True))
      if len(self.ranking) > self.limitSize:
        del self.ranking[-1]

  def enable_ranking(self):
    return self.ranking[0:self.enableSize]

  
  