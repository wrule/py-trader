from typing import Dict, Tuple
from random import randrange

IntScope = Dict[str, Tuple[int, int]]

class IntSpace:
  def __init__(self, scope: IntScope):
    self.scope = scope
  
  scope: IntScope
  
  def breadth(self):
    result = 1
    for value in self.scope.values():
      result = result * (abs(value[1] - value[0]) + 1)
    return result
  
  def random(self):
    result = { }
    for key, value in self.scope.items():
      result[key] = randrange(value[0], value[1] + 1)
    return result
