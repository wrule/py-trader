
import pandas as pd
import yfinance as yf

def download(symbol: str):
  print(f'{symbol}数据下载中...')
  ticker = yf.Ticker(symbol)
  hist = ticker.history(period = 'max')
  filePath = f'data/yahoo/{symbol}.pkl'
  hist.to_pickle(filePath)
  print(f'下载完成，数据已经保存在: {filePath}')
  
def load(symbol: str) -> pd.DataFrame:
  filePath = f'data/yahoo/{symbol}.pkl'
  return pd.read_pickle(filePath)
