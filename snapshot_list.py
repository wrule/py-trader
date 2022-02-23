
import pandas as pd
from pandas import DataFrame
from dataclasses import dataclass
from datetime import datetime

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
    self.df = self.toDataFrame(Snapshot())
    self.df.drop(self.df.index, axis = 0, inplace = True)
  
  df: DataFrame = None
  
  def toDataFrame(
    self,
    snapshot: Snapshot,
  ):
    df = DataFrame([snapshot])
    df.index = pd.to_datetime(df['datetime'])
    df.drop('datetime', axis = 1, inplace = True)
    return df


  def append(
    self,
    snapshot: Snapshot,
  ):
    self.df = pd.concat([self.df, self.toDataFrame(snapshot)])
    print(self.df)
