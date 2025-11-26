# build transition matrix
def buildtransitionmatrix(returnstates):
  transitions = np.zeros((6,6))
  upwards=0
  downwards=0
  # iterate through return
  n = len(returnstates)
  for i in range(n-1):
    prev = returnstates[i]
    next = returnstates[i+1]
    transitions[prev, next] = transitions[prev,next]+1
    # count the upward transitions
    if next < prev:
      upwards = upwards+1
    # count the downward transitions
    if prev > next:
      downwards = downwards+1
  # divide by rows
  n = len(transitions)
  for i in range(n):
    rowi = transitions[i,:]
    s = np.sum(rowi)
    #print(s)
    transitions[i] = transitions[i]/s
  return transitions, upwards, downwards
  
def getreturnstates(returns, mu, sd):
  n = len(returns)
  returnstates = []
  diffs = []
  # find means of each state
  statemeans = {}
  for i in range(6):
    statemeans[i] = []
  for i in range(n):
    # calculate the distance between jump and compare  to sd
    if i >0:
      diff = returns[i] - returns[i-1]
      fac = diff/sd # factor
      diffs.append(diff)

    if returns[i] > mu+sd :
      returnstates.append(0)
      s = statemeans[0]
      s.append(returns[i])
      statemeans[0] = s
    elif mu+0.5*sd <= returns[i] and returns[i] < mu+sd:
      returnstates.append(1)
      s= statemeans[1]
      s.append(returns[i])
      statemeans[1] = s
    elif mu <= returns[i] < mu+0.5*sd:
      returnstates.append(2)
      s= statemeans[2]
      s.append(returns[i])
      statemeans[2] = s
    elif mu-0.5*sd <= returns[i] < mu:
      returnstates.append(3)
      s= statemeans[3]
      s.append(returns[i])
      statemeans[3] = s
    elif mu - sd <= returns[i] < mu-0.5*sd:
      returnstates.append(4)
      s= statemeans[4]
      s.append(returns[i])
      statemeans[4] = s
    elif returns[i] < mu- sd:
      returnstates.append(5)
      s= statemeans[5]
      s.append(returns[i])
      statemeans[5] = s
  return returnstates # , statemeans, diffs


def get_transition_matrices(totallogreturns):
  returnstates_map = {}
  transitions_map = {}
  for i in range(8):
    returns = totallogreturns[i]
    mu_i = np.mean(returns)
    sd_i = np.std(returns)
    returnstates, statemeans, diffs = getreturnstates(returns, mu_i, sd_i)
    returnstates_map[i] = returnstates
    transition_mat, up, down = buildtransitionmatrix(returnstates)
    transitions_map[i] = transition_mat
  return transitions_map, returnstates_map
