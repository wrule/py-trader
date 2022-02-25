#!/opt/homebrew/bin/python3
from datetime import datetime
from tools.yfinance import load
from strategy.twoLinesCross import TwoLinesCross
from trader import Trader

df = load('BTC-USD')
df.ta.sma(length = 8, append = True)
df.ta.sma(length = 44, append = True)

# trader = Trader()
# tlc = TwoLinesCross(trader, 'SMA_8', 'SMA_44')
# print(datetime.now())
# tlc.Backtesting(df)
# print(datetime.now())
# print(trader.funds)
