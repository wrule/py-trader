
import pandas as pd
from pandas import DataFrame
from dataclasses import dataclass
import datetime

@dataclass
class Snapshot:
  datetime: datetime
  funds: float
  assets: float
  fundsDebt: float
  assetsDebt: float
  price: float

class SnapshotList:
  def __init__(
    self,
  ):
    self.df = DataFrame([Snapshot(0, 0, 0, 0, 0, 0)])
    self.df.index = pd.to_datetime(self.df['datetime'])
    self.df.drop('datetime', axis = 1, inplace = True)
    self.df.drop(self.df.index, inplace = True)
  
  df: DataFrame = None

  def append(
    self,
    snapshot: Snapshot,
  ):
    pd.concat()
    print(self.df)
