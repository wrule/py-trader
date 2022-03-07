#!/opt/homebrew/bin/python3
import math
from operator import mod
from typing import List
from numpy import append
import pandas_ta as ta
from tools.yfinance import to_dict_list
from tools.tradingview_csv import load
from trader import Trader
from strategy.twoLinesCross import TwoLinesCross
from strategy.history import History
import time
from random import randrange
import matplotlib.pyplot as plt
import numpy as np
from optimizer.int_scope import IntSpace

data_df = load('BINANCE_BTCUSDT, 120_cd3a1')

if __name__ == '__main__':
  scope1 = IntSpace({
    'p1': [1, 200],
    'p2': [1, 200],
  })
  scope2 = IntSpace({
    'p1': [1, 200],
    'p2': [1, 200],
  })
  print(scope1.distance(scope2.center()))
