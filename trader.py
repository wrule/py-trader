from datetime import datetime
from account.contract_account import ContractAccount
from account.spot_account import SpotAccount
from snapshot_list import Snapshot, SnapshotList
from transaction_list import TransactionList

class Trader:
  def __init__(
    self,
    contract: ContractAccount,
    spot: SpotAccount,
  ):
    self.contract = contract
    self.spot = spot
    self.snapshotList = SnapshotList()
    self.transactionList = TransactionList()

  contract: ContractAccount
  spot: SpotAccount
  snapshotList: SnapshotList
  transactionList: TransactionList
  
  def valuation(self, price: float):
    result = 0
    if self.contract is not None:
      result += self.contract.valuation(price)
    if self.spot is not None:
      result += self.spot.valuation(price)
    return result

  def make_snapshot(self, date: datetime, price: float):
    self.snapshotList.append(Snapshot(date, price, self.valuation(price)))
    
  def mk_snapshot(self, date: datetime, price: float):
    return Snapshot(date, price, self.valuation(price))
    
  def start(self, date: datetime, price: float):
    self.transactionList.start(self.mk_snapshot(date, price))
    
  def end(self, date: datetime, price: float):
    self.transactionList.end(self.mk_snapshot(date, price))
