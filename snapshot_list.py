
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
  
  def assetsValuation(self):
    return self.funds + self.assets * self.price
  
  def debtValuation(self):
    return self.fundsDebt + self.assetsDebt * self.price
  
  def valuation(self):
    return self.assetsValuation() - self.debtValuation()

class SnapshotList:
  list: List[Snapshot] = []

  def append(self, snapshot: Snapshot):
    self.list.append(snapshot)

  def dataframe(self):
    df = DataFrame(self.list)
    df.index = pd.to_datetime(df['datetime'])
    df.drop('datetime', axis = 1, inplace = True)
    df['assetValuation'] = df.apply(lambda row: row['funds'] + row['assets'] * row['price'], axis = 1)
    df['debtValuation'] = df.apply(lambda row: row['fundsDebt'] + row['assetsDebt'] * row['price'], axis = 1)
    df['valuation'] = df.apply(lambda row: row['assetValuation'] - row['debtValuation'], axis = 1)
    return df
