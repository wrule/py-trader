
import math
from typing import List
import pandas as pd
from pandas import DataFrame
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Snapshot:
  time: datetime
  funds: float = 0
  fundsDebt: float = 0
  assets: float = 0
  assetsDebt: float = 0
  price: float = 0
  
  def assetsValuation(self):
    return self.funds + self.assets * self.price
  
  def debtValuation(self):
    return self.fundsDebt + self.assetsDebt * self.price
  
  def valuation(self):
    return self.assetsValuation() - self.debtValuation()

class SnapshotList:
  def __init__(self):
    self.list = []
  
  list: List[Snapshot]

  def append(self, snapshot: Snapshot):
    self.list.append(snapshot)

  def last(self, index: int = 0):
    return self.list[-index - 1]
  
  def length(self):
    return len(self.list)
  
  def return_ratio(self, size: int = 7, offset: int = 0):
    width = self.length() - offset
    intervalNumber = int(width / size)
    startIndex = offset + width % size
    startValuation = self.list[startIndex].valuation()
    endValuation = self.last().valuation()
    profitRatio = endValuation / startValuation
    return math.pow(profitRatio, 1.0 / intervalNumber) - 1
    
    # for startIndex in range(0, len(self.list), size):
    #   endIndex = startIndex + size - 1
    #   if endIndex < len(self.list):
    #     startValuation = self.list[startIndex].valuation()
    #     endValuation = self.list[endIndex].valuation()
    #     profitRate = (endValuation - startValuation) / startValuation
    #     print(profitRate)
    # print(len(self.list))
    return 0
  
  def sharpe_ratio(self, size: int):
    return 0

  def dataframe(self):
    df = DataFrame(self.list)
    df.index = pd.to_datetime(df['time'])
    df['assetsValuation'] = [item.assetsValuation() for item in self.list]
    df['debtValuation'] = [item.debtValuation() for item in self.list]
    df['valuation'] = [item.valuation() for item in self.list]
    return df
