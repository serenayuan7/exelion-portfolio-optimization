def evaluate_signals(df):
  df['Returns'] = df['Close'].pct_change()
  df['Strategy Returns'] = df['Signal'].shift(1) * df['Returns']
  
  df['Cumulative Returns'] = (1 + df['Strategy Returns']).cumprod()
  
  # Bollinger bands on Weibo data 4 hour
  plt.plot(df.index, df['Cumulative Returns'], label='Cumulative Returns', color='green', linewidth=2)
  plt.show()

  return df
