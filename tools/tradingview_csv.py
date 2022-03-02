import pandas as pd

def load(name: str):
  df = pd.read_csv(f'data/tradingview/{name}.csv')
  df.drop('Volume MA', axis = 1, inplace = True)
  df.rename(
    columns = {
      'time': 'Date',
      'open': 'Open',
      'high': 'High',
      'low': 'Low',
      'close': 'Close',
    },
    inplace = True,
  )
  df.index = pd.to_datetime(df['Date'], unit = 's')
  df['Date'] = df.index
  return df
