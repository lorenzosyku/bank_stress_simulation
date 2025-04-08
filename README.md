# 🏦 Bank Capital Stress Simulation

A Python simulation tool that models how bank capital is affected by market drawdowns under various interest rate and volatility regimes.

## 📈 What It Does

- Simulates daily returns on bank-held assets
- Tracks capital drawdown vs. liabilities
- Triggers "margin call" style stress when capital falls below a threshold
- Supports configurable parameters: leverage, interest rates, volatility
- Plots asset value trajectories over time

## 🧠 Conceptual Model

This project uses a basic stress-testing model where:

- Bank starts with $100M in equity and 10x leverage
- Simulated market returns affect asset value daily
- Capital buffer is monitored — if it falls below 20%, a "margin call" is triggered
- Interest rates and volatility are fully adjustable

## ▶️ How to Run

1. **Clone the project**  
   ```bash
   git clone https://github.com/your-username/bank_stress_sim.git
   cd bank_stress_sim

   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

   pip install -r requirements.txt

   python main.py


