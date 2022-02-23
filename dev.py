#!/opt/homebrew/bin/python3
from cmath import nan
import pandas as pd
import pandas_ta as ta
from tools.yfinance import load
from strategy.strategy import Strategy
from strategy.twoLinesCross import TwoLinesCross

df1 = load('BTC-USD')
# df.ta.sma(length = 8, append = True)
# df.ta.sma(length = 44, append = True)

# s = TwoLinesCross('SMA_8', 'SMA_44')
# s.Backtesting(df)

print('你好，世界')

df = pd.DataFrame()
newRow = pd.DataFrame({
  'age': range(10),
  'name': [f'第{x + 1}个' for x in range(10)],
})
# df.append(newRow)
print(newRow)
# print(df1)