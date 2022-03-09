from collections.abc import Callable
from typing import List, Tuple
from optimizer.int_space import IntPoint, IntSpace
from bisect import bisect
from optimizer.int_ranking import Record, IntRanking

def rankingPush(
  ranking: List[Tuple[IntPoint, float]],
  point: IntSpace,
  score: float,
  limit: int = 5,
):
  ranking.append((point, score))
  ranking.sort(key = lambda t: t[1], reverse = True)
  if len(ranking) > limit:
    del ranking[limit]

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
    
  def spaceExplore(
    self,
    space: IntSpace,
    func: Callable[..., float],
  ):
    ranking = IntRanking()
    for i in range(self.batchSize):
      point = space.random()
      score = func(**point)
      ranking.try_push(point, score)
      print(i)
    for record in ranking.enable_ranking():
      sub_space = self.space.sub_space(record[0], 0.1)
      print(record)
      print(sub_space.scope)
      sub_ranking = self.spaceExplore(sub_space, func)
    return ranking
  
  
  def explore(
    self,
    func: Callable[..., float],
  ):
    ranking = self.spaceExplore(self.space, func)
    # print(ranking.ranking)

