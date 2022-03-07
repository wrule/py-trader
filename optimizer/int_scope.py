from typing import Dict, Tuple
from random import randrange
import math

IntPoint = Dict[str, int]
IntScope = Dict[str, Tuple[int, int]]

def point_to_scope(point: IntPoint, radius: int) -> IntScope:
  pass

class IntSpace:
  def __init__(self, scope: IntScope):
    self.scope = scope
  
  scope: IntScope
  
  def center(self) -> IntPoint:
    result: IntPoint = { }
    for key, value in self.scope.items():
      result[key] = value[0] + int((value[1] - value[0]) / 2)
    return result
  
  def breadth(self) -> int:
    result = 1
    for value in self.scope.values():
      result = result * (value[1] - value[0] + 1)
    return result
  
  def random(self) -> IntPoint:
    result: IntPoint = { }
    for key, value in self.scope.items():
      result[key] = randrange(value[0], value[1] + 1)
    return result

  def distance(self, center: IntPoint) -> int:
    myCenter = self.center()
    sum = 0
    for key in myCenter.keys():
      v1 = myCenter[key]
      v2 = center[key]
      sum += math.pow(v1 - v2, 2)
    return math.sqrt(sum)
  
  def intersection(self, space):
    result = { }
    otherScope = space.scope
    for key in self.scope.keys():
      [min1, max1] = self.scope[key]
      [min2, max2] = otherScope[key]
      min = min1 if min1 > min2 else min2
      max = max1 if max1 < max2 else max2
      result[key] = (min, max)
    return IntSpace(result)
