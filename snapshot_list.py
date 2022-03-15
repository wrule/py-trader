
import math
from typing import List
import pandas as pd
from pandas import DataFrame
from dataclasses import dataclass
from datetime import datetime
import numpy

@dataclass
class Snapshot:
  time: datetime
  valuation: float
  price: float = 0

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
    startValuation = self.list[startIndex].valuation
    endValuation = self.last().valuation
    profitRatio = endValuation / startValuation
    return math.pow(profitRatio, 1.0 / intervalNumber) - 1
  
  def return_ratio_std(self, size: int = 7, offset: int = 0):
    profitRatioList: List[float] = []
    for endIndex in range(
      self.length() - 1,
      -1,
      -(size - 1),
    ):
      startIndex = endIndex - (size - 1)
      if startIndex >= offset:
        startValuation = self.list[startIndex].valuation
        endValuation = self.list[endIndex].valuation
        profitRatio = (endValuation - startValuation) / startValuation
        profitRatioList.append(profitRatio)
      else:
        break
    return numpy.std(profitRatioList)
    
    
    # width = self.length() - offset
    # # intervalNumber = int(width / size)
    # startIndex = offset + width % size
    # profitRatioList: List[float] = []
    # for currentIndex in range(startIndex, self.length(), size - 1):
    #   endIndex = currentIndex + size - 1
    #   currentValuation = self.list[currentIndex].valuation
    #   endValuation = self.list[endIndex].valuation
    #   profitRatio = (endValuation - currentValuation) / currentValuation
    #   profitRatioList.append(profitRatio)
    # print(profitRatioList)
    # return numpy.std(profitRatioList)
  
  def sharpe_ratio(self, size: int = 7, offset: int = 0):
    return self.return_ratio(size, offset) / self.return_ratio_std(size, offset)

  def dataframe(self):
    df = DataFrame(self.list)
    df.index = pd.to_datetime(df['time'])
    return df
