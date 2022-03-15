from account.contract_account import ContractAccount
from account.spot_account import SpotAccount

class Trader:
  def __init__(
    self,
    contract: ContractAccount,
    spot: SpotAccount,
  ):
    self.contract = contract
    self.spot = spot

  contract: ContractAccount
  spot: SpotAccount
  
  def valuation(self, price: float):
    result = 0
    if self.contract is not None:
      result += self.contract.valuation(price)
    if self.spot is not None:
      result += self.spot.valuation(price)
    return result
