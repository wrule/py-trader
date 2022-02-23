from pandas import DataFrame

class Strategy:
  def __init__(self):
    pass
  
  hist: DataFrame = None
  
  def length(
    self,
  ):
    return len(self.hist.index)
  
  def row(
    self,
    index: int,
  ):
    return self.hist.iloc[index]
  
  def last(
    self,
    field: str,
  ):
    return self.hist.tail(2)[field].iloc[1]
  
  def prev(
    self,
    field: str,
  ):
    return self.hist.tail(2)[field].iloc[0]
  
  def Backtesting(
    self,
    hist: DataFrame,
  ):
    for index in range(len(hist.index)):
      self.hist = hist.iloc[0 : index + 1]
      print(len(self.hist.index), self.last('SMA_8'), self.last('SMA_44'))
