from datetime import datetime
from typing import List
from unittest import result
from stock.contract import Contract

class ContractAccount:
  def __init__(
    self,
    funds: float,
    lever: int,
    unit: float,
    buy_fee: float,
    sell_fee: float,
  ):
    self.funds = funds
    self.lever = lever
    self.unit = unit
  
  funds: float
  lever: int
  unit: float
  contract_list: List[Contract]
  
  def lever_funds(self):
    return self.funds * self.lever
  
  def available_funds(
    self,
    price: float,
  ):
    result = self.lever_funds()
    for contract in self.contract_list:
      result -= contract.deposit(price)
      result += contract.profit(price)
    return result
      
  def short(
    self,
    use_funds: float,
    price: float,
    date: datetime,
  ):
    available_funds = self.available_funds(price)
    if available_funds <= 0:
      return None
    use_funds = (
      use_funds
      if use_funds <= available_funds
      else available_funds
    )
    get_assets = int(use_funds / price / self.unit) * self.unit
    contract = Contract(get_assets, price, date, self.lever, -1)
    self.contract_list.append(contract)
    return (use_funds, get_assets)

  
  