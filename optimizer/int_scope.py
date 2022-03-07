from typing import Dict, Tuple

IntScope = Dict[str, Tuple[int, int]]

class IntSpace:
  def __init__(self, scope: IntScope):
    self.scope = scope
  
  scope: IntScope
  
  def breadth(self):
    return 0
  
  def random(self):
    return { }