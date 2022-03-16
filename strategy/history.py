from typing import Any, Dict, List
from pandas import DataFrame
from tools.yfinance import to_dict_list

class History:
  def __init__(self, df: DataFrame):
    self.df = df
    self.data = to_dict_list(self.df)
    self.lastIndex = 0
  
  df: DataFrame
  data: List[Dict[str, Any]]
  lastIndex: int
  
  def last(self, index: int = 0):
    return self.data[self.lastIndex - index]

  def prev(self):
    return self.last(1)

  def length(self):
    return len(self.data)

  def show(self):
    print('可视化显示')
    pass
