# market_scenarios.py
import numpy as np

def simulate_market_returns(volatility, years, steps_per_year=252):
    dt = 1 / steps_per_year
    steps = int(years * steps_per_year)
    returns = np.random.normal(loc=0, scale=volatility * np.sqrt(dt), size=steps)
    return returns
