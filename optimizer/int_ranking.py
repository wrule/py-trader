
from typing import List, Tuple
from optimizer.int_space import IntPoint

Record = Tuple[IntPoint, float, bool]

class IntRanking:
  def __init__(self, limit: int = 10):
    self.limit = limit
    self.ranking = []
  
  ranking: List[Record]
  limit: int
  
  def first(self):
    return self.ranking[0]
  
  def last(self):
    return self.ranking[-1]
  
  def try_push(self, point: IntPoint, score: int):
    if (
      len(self.ranking) < self.limit or
      score > self.last()[1]
    ):
      index = 0
      for item in self.ranking:
        if score > item[1]:
          break
        index += 1
      self.ranking.insert(index, (point, score, True))
      if len(self.ranking) > self.limit:
        del self.ranking[-1]


  
  