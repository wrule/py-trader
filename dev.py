#!/opt/homebrew/bin/python3
from account.contract_account import ContractAccount
from account.spot_account import SpotAccount

if __name__ == '__main__':
  account = SpotAccount(100, 0.001, 0.001)
  account.buy_funds(50, 1, None)
  print(account.funds)
  print(account.spot_list[0])
