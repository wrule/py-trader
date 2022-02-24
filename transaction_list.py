
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
  start: datetime
  end: datetime
  startFunds: float = 0
  startAssets: float = 0
  startFundsDebt: float = 0
  startAssetsDebt: float = 0
  startPrice: float = 0
  endFunds: float = 0
  endAssets: float = 0
  endFundsDebt: float = 0
  endAssetsDebt: float = 0
  endPrice: float = 0

class TransactionList:
  def __init__(self):
    pass
