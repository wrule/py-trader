from typing import Any, Dict, List
from matplotlib.pyplot import title
from pandas import DataFrame
from tools.yfinance import to_dict_list
import mplfinance as mpf

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
    df = self.df[5000:5400]
    print(df)
    ap2 = [
      mpf.make_addplot(df['STOCHRSIk_49_8_8_27'], color = 'g', panel = 2),
      mpf.make_addplot(df['STOCHRSId_49_8_8_27'], color = 'b', panel = 2),
    ]
    mpf.plot(
      df,
      type = 'candle',
      volume = True,
      style = 'binance',
      # title = 'kline',
      # figscale = 1,
      # figratio = (2.5, 1),
      # ylabel = '你好',
      datetime_format = '%m-%d %H:%M',
      main_panel=1,volume_panel=0,
      addplot=ap2,
    )
    pass
