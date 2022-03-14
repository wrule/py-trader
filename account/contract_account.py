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
    fee: float,
    funds_fee: float,
  ):
    self.funds = funds
    self.lever = lever
    self.unit = unit
    self.fee = fee
    self.funds_fee = funds_fee
    self.contract_list = []
  
  funds: float
  lever: int
  unit: float
  fee: float
  funds_fee: float
  contract_list: List[Contract]
  
  def available_funds(self, price: float):
    result = self.funds
    for contract in self.contract_list:
      result -= contract.deposit(price)
      result += contract.profit(price)
    result = result if result >= 0 else 0
    return result
  
  def lever_funds(self, price: float):
    return self.available_funds(price) * self.lever
  
  def buy_funds(
    self,
    direction: int,
    use_funds: float,
    price: float,
    date: datetime,
  ):
    lever_funds = self.lever_funds(price)
    if lever_funds <= 0:
      return None
    use_funds = (
      use_funds
      if use_funds <= lever_funds
      else lever_funds
    )
    get_assets = int(use_funds / price / self.unit) * self.unit
    use_funds = get_assets * price
    use_fee = use_funds * self.fee
    if self.funds < use_fee:
      return None
    self.funds -= use_fee
    contract = Contract(get_assets, price, date, self.lever, direction)
    self.contract_list.append(contract)
    return (use_funds, get_assets)

  def long(
    self,
    use_funds: float,
    price: float,
    date: datetime,
  ):
    return self.buy_funds(1, use_funds, price, date)

  def short(
    self,
    use_funds: float,
    price: float,
    date: datetime,
  ):
    return self.buy_funds(-1, use_funds, price, date)

  def close(self, index: int, price: float):
    current_valuation = self.contract_list[index].current_valuation(price)
    profit = self.contract_list[index].profit(price)
    self.funds += profit
    self.funds -= current_valuation * self.fee
    del self.contract_list[index]
    if self.funds < 0:
      self.funds = 0
    return (current_valuation, profit)

  def close_all(self, price: float):
    current_valuation_total = 0
    profit_total = 0
    while len(self.contract_list) > 0:
      (current_valuation, profit) = self.close(0, price)
      current_valuation_total += current_valuation
      profit_total += profit
    return (current_valuation_total, profit_total)

  def valuation(self, price: float):
    result = self.funds
    for contract in self.contract_list:
      result += contract.profit(price)
    return result
  
  def nominal_valuation(self, price: float):
    result = 0
    for contract in self.contract_list:
      result += contract.current_valuation(price)
    return result

  def deduct_funds_fee(self, price: float):
    self.funds -= self.nominal_valuation(price) * self.funds_fee
    if self.funds < 0:
      self.funds = 0
