from pandas import DataFrame

class Strategy:
  def __init__(self):
    pass
  
  hist: DataFrame = None
  
  def Backtesting(
    self,
    hist: DataFrame,
  ):
    for index in range(len(hist.index)):
      currentHist: DataFrame = hist.iloc[0 : index + 1]
      print(len(currentHist.index))
    print(hist.iloc[0])
