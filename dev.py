#!/opt/homebrew/bin/python3
import pandas as pd
from tools.tradingview_csv import load

df = load('BINANCE_BTCUSDT, 120')
print(df)
