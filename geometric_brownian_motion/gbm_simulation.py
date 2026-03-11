import numpy as np
import matplotlib.pyplot as plt

class GBMSimulator:
    def __init__(self, s0=100.0, mu=0.08, sigma=0.2, T=1.0, trading_days=252):
        self.s0 = s0
        self.mu = mu
        self.sigma = sigma
        self.T = T
        self.dt = T / trading_days
        self.steps = trading_days
    
    def generate_paths(self, n_paths=10000):
        z = np.random.normal(loc=0.0, scale=1.0, size=(n_paths, self.steps))
        drift = (self.mu - 0.5 * self.sigma ** 2) * self.dt
        diffusion = self.sigma * np.sqrt(self.dt) * z
        daily_log_returns = drift + diffusion
        cum_log_returns = np.cumsum(daily_log_returns, axis=1)
        price_paths = self.s0 * np.exp(cum_log_returns)
        return np.insert(price_paths, 0, self.s0, axis=1)

if __name__ == '__main__':
    sim_1 = GBMSimulator(s0=100, mu=0.08, sigma=0.15)
    paths_1 = sim_1.generate_paths(n_paths=100000)
    final_1 = paths_1[:,-1]

    sim_2 = GBMSimulator(s0=100, mu=0.25, sigma=0.10)
    paths_2 = sim_2.generate_paths(n_paths=100000)
    final_2 = paths_2[:,-1]

    sim_3 = GBMSimulator(s0=100, mu=0.08, sigma=0.50)
    paths_3 = sim_3.generate_paths(n_paths=100000)
    final_3 = paths_3[:,-1]

    plt.figure(figsize=(12, 7))
    bins = np.linspace(0, 300, 150)
    plt.hist(final_1, bins=bins, alpha=0.5, color='blue', edgecolor='black', lw=0.5, density=True, label=r'mu=8%, sigma=15%')
    plt.hist(final_2, bins=bins, alpha=0.5, color='red', edgecolor='black', lw=0.5, density=True, label=r'mu=25%, sigma=10%')
    plt.hist(final_3, bins=bins, alpha=0.5, color='green', edgecolor='black', lw=0.5, density=True, label=r'mu=8%, sigma=50%')
    plt.axvline(x=100, color='black', linestyle='--', linewidth=1, label='S[0]')
    plt.grid(True, alpha=0.4)
    plt.xlim(0, 300)
    plt.tight_layout()
    plt.show()
