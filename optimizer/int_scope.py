from typing import Dict, Tuple
from random import randrange

IntScope = Dict[str, Tuple[int, int]]

class IntSpace:
  def __init__(self, scope: IntScope):
    self.scope = scope
  
  scope: IntScope
  
  def breadth(self):
    return 0
  
  def random(self):
    result = { }
    for key, value in self.scope.items():
      result[key] = randrange(value[0], value[1] + 1)
    return result
