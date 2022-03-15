#!/opt/homebrew/bin/python3
from account.contract_account import ContractAccount
from account.spot_account import SpotAccount

if __name__ == '__main__':
  account = ContractAccount(100, 3, 0.01, 0.0002)
  print(account.long(285, 13.07, None))
  print(account.close_all(15.00))
