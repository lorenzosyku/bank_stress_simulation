# main.py

import matplotlib.pyplot as plt
from stress_simulation import simulate_bank_drawdown
from config import INTEREST_RATE, VOLATILITY, SIM_YEARS

def main():
    paths = []
    margin_called = []

    for _ in range(10):  # simulate 10 paths
        values, called = simulate_bank_drawdown(INTEREST_RATE, VOLATILITY, SIM_YEARS)
        paths.append(values)
        margin_called.append(called)

    for i, path in enumerate(paths):
        plt.plot(path, label=f'Run {i+1}{" (MC)" if margin_called[i] else ""}')

    plt.title("Bank Asset Value Trajectories")
    plt.xlabel("Days")
    plt.ylabel("Asset Value ($)")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
