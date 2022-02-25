#!/opt/homebrew/bin/python3
from datetime import datetime
import pandas_ta as ta
from tools.yfinance import load, to_dict_list
from strategy.twoLinesCross import TwoLinesCross
from trader import Trader

df = load('BTC-USD')
df.ta.sma(length = 8, append = True)
df.ta.sma(length = 44, append = True)

hist = to_dict_list(df)

trader = Trader()
tlc = TwoLinesCross(trader, 'SMA_8', 'SMA_44')
oldTime = datetime.now()
tlc.Backtesting(hist)
print(datetime.now() - oldTime)
print(trader.funds)
