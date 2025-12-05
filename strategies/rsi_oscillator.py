from rsi import calculate_rsi
def rsi_oscillator(df):
  df['SMA200'] = df['Close'].rolling(window=200).mean()
  df['RSI'] = calculate_rsi(df)
  signals=[]
  if rsi_val < 30 and prices[i] > sma200:
    signals.append(1) #buy
  # exit the market when rsi > 70 and price below sma200
  elif rsi_val > 70 and prices[i] < sma200:
    signals.append(-1)
  else:
    signals.append(0)
  df['Signal'] = signals
  return df
