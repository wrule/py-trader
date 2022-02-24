
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
  beforeDatetime: datetime
  afterDatetime: datetime
  beforeFunds: float = 0
  beforeAssets: float = 0
  beforeFundsDebt: float = 0
  beforeAssetsDebt: float = 0
  beforePrice: float = 0
  afterFunds: float = 0
  afterAssets: float = 0
  afterFundsDebt: float = 0
  afterAssetsDebt: float = 0
  afterPrice: float = 0

class TransactionList:
  def __init__(self):
    pass
