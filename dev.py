#!/opt/homebrew/bin/python3
from tools.yfinance import load, download

if __name__ == '__main__':
  df = load('BTC-USD')
  print(df)
