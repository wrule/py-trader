#!/opt/homebrew/bin/python3
from turtle import down
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import mplcursors
import mplfinance as mpf
from tools.yfinance import load as yhload, download
from tools.tradingview_csv import load as tvload

df1 = yhload('BTC-USD')
print(df1)
df2 = tvload('BINANCE_BTCUSDT, 120')
print(df2)
df1 = df1.tail(100)
mpf.plot(df1, type = 'candle', volume = True)
# fig, ax = plt.subplots()
# fig.set_size_inches(8, 4)
# fig.canvas.manager.set_window_title('简单折线图')
# ax.plot([0, 1, 2, 3, 4], [1, 4, 2, 3, 9]);
# ax.legend()
# mplcursors.cursor(hover = True)
# plt.show()
