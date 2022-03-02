#!/opt/homebrew/bin/python3
import pandas as pd
import pandas_ta as ta
from tools.yfinance import load

df = load('BTC-USD')
df.ta.log_return(cumulative = True, append = True)
df.ta.percent_return(cumulative = True, append = True)
df.ta.ema(length = 20, append = True)
print(df.tail(10))
