import numpy as np
def rsi(prices):
  # average gain
  again = []
  aloss = []
  n = len(prices) # number of periods
  for i in range(n-1):
    pnext = prices[i+1]
    pnow = prices[i]
    if pnext> pnow:
      again.append(pnext- pnow)
    else:
      aloss.append(pnow - pnext)
  gains = np.sum(again)
  losses = np.sum(aloss)
  ag = gains/n
  al = losses/n
  rel_strength = ag/al
  rsi = 100 - (100/(1+rel_strength))
  return rsi

import pandas as pd

def calculate_rsi(prices, period=14):
    """
    Calculates the Relative Strength Index (RSI) for a given series of prices.

    Args:
        prices (pd.Series): A series of closing prices.
        period (int): The number of periods for the RSI calculation (default: 14).

    Returns:
        pd.Series: A series containing the RSI values.
    """
    deltas = prices.diff()

    gains = deltas.mask(deltas < 0, 0)
    losses = -deltas.mask(deltas > 0, 0)

    # Initial averages (simple moving average for the first 'period' values)
    avg_gain = gains.ewm(com=period - 1, adjust=False).mean()
    avg_loss = losses.ewm(com=period - 1, adjust=False).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return rsi
