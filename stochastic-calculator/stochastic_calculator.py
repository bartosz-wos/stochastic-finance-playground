import numpy as np
import matplotlib.pyplot as plt

def stochastic_calc(n_sim=100000):
    revenue = np.random.normal(loc=100000, scale=20000, size=n_sim)
    costs = np.random.uniform(low=50000, high=80000, size=n_sim)
    black_swan_pen = np.random.choice([0, 40000], size=n_sim, p=[0.95, 0.05])
    return revenue - costs - black_swan_pen

profits = stochastic_calc()
expected_profit = np.mean(profits)
prob_of_loss = np.mean(profits < 0) * 100

print(expected_profit)
print(prob_of_loss)

plt.figure(figsize=(12, 6))
plt.hist(profits, bins=100, color='blue', edgecolor='black', alpha=0.6)

plt.axvline(x=0, color='red', linestyle='--', linewidth=1, label='loss thresh')
plt.axvline(x=expected_profit, color='green', linestyle='-', linewidth=1, label='expected profit')
plt.grid(True, alpha=0.4)
plt.tight_layout()
plt.show()
