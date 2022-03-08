
from typing import List, Tuple
from int_space import IntPoint

Record = Tuple[IntPoint, int, bool]

class IntRanking:
  def __init__(self, limit: int = 10):
    self.limit = limit
  
  ranking: List[Record]
  limit: int
  
  def first(self):
    return self.ranking[0]
  
  def last(self):
    return self.ranking[-1]
  
  def try_push(self, point: IntPoint, score: int):
    if len(self.ranking) < self.limit:
      self.ranking.append((point, score, True))
    else:
      pass
    pass
  
  