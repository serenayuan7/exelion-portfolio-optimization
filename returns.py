import numpy as np
def get_returns(prices):
  n = len(prices)
  returns = []
  for i in range(1,n):
    ret = (p[i] - p[i-1])/p[i-1]
    returns.append(ret)
  return returns

def get_log_returns(prices):
  n = len(prices)
  returns = []
  for i in range(1, n):
    logret = np.log(prices[i]) - np.log(prices[i-1])
    returns.append(logret)
  return returns
