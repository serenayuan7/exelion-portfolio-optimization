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
