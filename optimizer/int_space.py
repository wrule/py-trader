from typing import Dict, Tuple
from random import randrange
import math

IntPoint = Dict[str, int]
IntScope = Dict[str, Tuple[int, int]]

class IntSpace:
  def __init__(self, scope: IntScope):
    self.scope = scope
  
  scope: IntScope
  
  def center(self) -> IntPoint:
    result: IntPoint = { }
    for key, value in self.scope.items():
      result[key] = value[0] + int((value[1] - value[0]) / 2)
    return result
  
  def breadth(self, density: float = 1) -> int:
    result = 1
    for value in self.scope.values():
      result = result * (value[1] - value[0] + 1)
    result = int(result * density)
    return result
  
  def random(self) -> IntPoint:
    result: IntPoint = { }
    for key, value in self.scope.items():
      result[key] = randrange(value[0], value[1] + 1)
    return result

  def distance(self, space) -> int:
    return point_distance(self.center(), space.center())
  
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

def point_to_space(point: IntPoint, diameter: int) -> IntSpace:
  scope = { }
  left = int((diameter - 1) / 2)
  right = diameter - left
  for key, value in point.items():
    scope[key] = (value - left, value + right)
  return IntSpace(scope)

def point_distance(point1: IntPoint, point2: IntPoint) -> int:
  sum = 0
  for key in point1.keys():
    v1 = point1[key]
    v2 = point2[key]
    sum += math.pow(v1 - v2, 2)
  return math.sqrt(sum)
