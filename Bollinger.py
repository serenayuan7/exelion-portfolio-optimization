def bollinger_bands(df, windowsize=10):
  import pandas as pd
  import matplotlib.pyplot as plt
  import numpy as np
  from returns import get_log_returns
  # Calculate the 20-period Simple Moving Average (SMA)
  df['returns'] = get_log_returns(df['Close'])
  df['SMA'] = df['Close'].rolling(window= windowsize).mean()
  
  # Calculate the 20-period Standard Deviation (SD)
  df['SD'] = df['Close'].rolling(window= windowsize).std()
  
  # Calculate the Upper Bollinger Band (UB) and Lower Bollinger Band (LB)
  df['UB'] = df['SMA'] + 2 * df['SD']
  df['LB'] = df['SMA'] - 2 * df['SD']
  
  # Create a column to store trading signals
  df['Signal'] = 0 # Initialise with no signal
  
  # Buy signal: Price touches or crosses below the lower band
  df.loc[df['Close'] <= df['LB'], 'Signal'] = 1
  
  # Sell signal: Price touches or crosses above the upper band
  df.loc[df['Close'] >= df['UB'], 'Signal'] = -1
  
  df['Returns'] = df['Close'].pct_change()
  df['Strategy Returns'] = df['Signal'].shift(1) * df['Returns']
  
  df['Cumulative Returns'] = (1 + df['Strategy Returns']).cumprod()
  
  # Bollinger bands on Weibo data 4 hour
  plt.plot(df.index, df['Cumulative Returns'], label='Cumulative Returns', color='green', linewidth=2)
  plt.show()

  return df
