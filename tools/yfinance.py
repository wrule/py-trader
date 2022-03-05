
import pandas as pd
from pandas import DataFrame
import yfinance as yf
from numba_try.kline import KLine
from datetime import datetime
from numba import types

def download(symbol: str):
  print(f'{symbol}数据下载中...')
  ticker = yf.Ticker(symbol)
  hist: pd.DataFrame = ticker.history(period = 'max')
  hist['Date'] = hist.index
  filePath = f'data/yahoo/{symbol}.pkl'
  hist.to_pickle(filePath)
  print(f'下载完成，数据已经保存在: {filePath}')
  
def load(symbol: str) -> DataFrame:
  filePath = f'data/yahoo/{symbol}.pkl'
  return pd.read_pickle(filePath)

def to_dict_list(df: DataFrame):
  return df.to_dict('records')


def to_kline_list(df: DataFrame):
  dict_list = to_dict_list(df)
  return [
    KLine(
      time = int(item['Date'].to_pydatetime().timestamp()),
      open = item['Open'],
      high = item['High'],
      low = item['Low'],
      close = item['Close'],
      volume = item['Volume'],
      closed = True,
    ) for item in dict_list
  ]

def load_dict_list(symbol: str):
  return to_dict_list(load(symbol))
