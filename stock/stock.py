from datetime import datetime
from abc import ABC, abstractmethod

class Stock(ABC):
  def __init__(
    self,
    volume: float,
    restockTime: datetime,
    restockPrice: float,
  ):
    self.volume = volume
    self.restockTime = restockTime
    self.restockPrice = restockPrice
  
  volume: float
  restockTime: datetime
  restockPrice: float

  @abstractmethod
  def start_valuation(self):
    return 0

  @abstractmethod
  def current_valuation(self):
    return 0

  def profit(self):
    return self.current_valuation() - self.start_valuation()