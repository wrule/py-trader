
import pandas as pd
from pandas import DataFrame
from dataclasses import dataclass
import datetime

@dataclass
class Snapshot:
  datetime: datetime = 0
  funds: float = 0
  assets: float = 0
  fundsDebt: float = 0
  assetsDebt: float = 0
  price: float = 0

class SnapshotList:
  def __init__(
    self,
  ):
    self.df = DataFrame([Snapshot()])
    self.df.index = pd.to_datetime(self.df['datetime'])
    self.df.drop('datetime', axis = 1, inplace = True)
    self.df.drop(self.df.index, axis = 0, inplace = True)
  
  df: DataFrame = None

  def append(
    self,
    snapshot: Snapshot,
  ):
    # pd.concat()
    print(self.df)
