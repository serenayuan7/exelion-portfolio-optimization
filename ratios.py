import pandas as pd
import numpy as np

def sortino_ratio(returns, target_return=0, annualization_factor=252):
    """
    Calculates the annualized Sortino ratio of a return series.

    Args:
        returns (pd.Series or np.array): A series of periodic (e.g., daily) returns.
        target_return (float): The minimum acceptable return (MAR), often the
                               risk-free rate. Default is 0.
        annualization_factor (int): The number of periods in a year
                                    (e.g., 252 for daily, 12 for monthly).

    Returns:
        float: The annualized Sortino ratio.
    """
    # Calculate the excess returns relative to the target return
    excess_returns = returns - target_return

    # Calculate the downside returns (returns below the target return)
    # Only consider negative deviations for downside deviation calculation
    downside_returns = np.minimum(0, excess_returns)

    # Calculate the downside deviation (standard deviation of downside returns)
    # The degrees of freedom (ddof) is set to 0 for population std deviation
    # relevant for historical data
    downside_deviation = np.std(downside_returns, ddof=0)

    # Handle cases with no downside deviation to avoid division by zero
    if downside_deviation == 0:
        return np.nan  # Return NaN or some other appropriate value

    # Calculate the Sortino ratio (mean excess return / downside deviation)
    # and annualize it using the square root of the annualization factor
    # Note: Annualize the mean return by multiplying by the factor,
    # annualize the std dev by multiplying by the sqrt of the factor
    # and simplify the final result as shown below for an annualized ratio
    sortino_ratio_value = np.mean(excess_returns) / downside_deviation

    # Annualize the final ratio
    annualized_sortino_ratio = sortino_ratio_value * np.sqrt(annualization_factor)

    return annualized_sortino_ratio
