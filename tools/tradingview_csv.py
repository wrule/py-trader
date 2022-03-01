import pandas as pd

def load(name: str):
  df = pd.read_csv(f'data/tradingview/{name}.csv')
  df.drop('Volume MA', axis = 1, inplace = True)
  df.rename(
    columns = {
      'time': 'datetime',
      'Volume': 'volume',
    },
    inplace = True,
  )
  df.index = pd.to_datetime(df['datetime'], unit = 's')
  df['datetime'] = df.index
  return df
