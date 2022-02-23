
from typing import List
import pandas as pd
from pandas import DataFrame
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Snapshot:
  datetime: datetime
  funds: float = 0
  assets: float = 0
  fundsDebt: float = 0
  assetsDebt: float = 0
  price: float = 0

  def valuation(self):
    totalFunds = self.funds + self.assets * self.price
    totalDebt = self.fundsDebt + self.assetsDebt * self.price
    return totalFunds - totalDebt

class SnapshotList:
  list: List[Snapshot] = []

  def append(self, snapshot: Snapshot):
    self.list.append(snapshot)  

  def dataframe(self):
    df = DataFrame(self.list)
    df.index = pd.to_datetime(df['datetime'])
    df.drop('datetime', axis = 1, inplace = True)
    return df
