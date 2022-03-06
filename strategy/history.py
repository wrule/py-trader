from typing import Any, Dict, List

class History:
  def __init__(self, data: List[Dict[str, Any]]):
    self.data = data
    self.lastIndex = 0
  
  data: List[Dict[str, Any]]
  lastIndex: int
  
  def last(self, index: int = 0):
    return self.data[self.lastIndex - index]

  def prev(self):
    return self.last(1)

  def length(self):
    return len(self.data)
