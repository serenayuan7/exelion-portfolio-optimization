# Define a simple trading strategy based on yield curve steepness
def trading_strategy(steepness, threshold=0.5):
    # Create signals: 1 for buy (long), -1 for sell (short), 0 for hold
    signals = np.where(steepness > threshold, 1, 0)  # Buy when steepness > threshold
    signals = np.where(steepness < -threshold, -1, signals)  # Sell when steepness < -threshold
    return signals
