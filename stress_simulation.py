# stress_simulation.py

import numpy as np
from config import INITIAL_BANK_CAPITAL, LEVERAGE_RATIO, MARGIN_THRESHOLD
from market_scenarios import simulate_market_returns

def simulate_bank_drawdown(interest_rate, volatility, years):
    equity = INITIAL_BANK_CAPITAL
    assets = equity * LEVERAGE_RATIO
    liabilities = assets - equity
    returns = simulate_market_returns(volatility, years)
    
    asset_values = [assets]

    for r in returns:
        assets *= (1 + r)
        equity = assets - liabilities
        asset_values.append(assets)

        if equity / assets < MARGIN_THRESHOLD:
            return asset_values, True  # Margin call triggered

    return asset_values, False
