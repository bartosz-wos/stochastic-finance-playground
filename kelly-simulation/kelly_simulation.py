import numpy as np
import matplotlib.pyplot as plt

def kelly_sim(p=0.6, b=1.0, steps=500):
    flips_1 = np.random.choice([1, -1], size=steps, p=[p, 1-p])
    flips_2 = np.random.choice([1, -1], size=steps, p=[p, 1-p])
    flips_3 = np.random.choice([1, -1], size=steps, p=[p, 1-p])
    kelly_fraction = p - (1 - p) / b
    capital_1 = [1000.0]
    capital_2 = [1000.0]
    capital_3 = [1000.0]
    
    f_1 = 0.05
    f_2 = kelly_fraction
    f_3 = 0.40
    
    for i in range(steps):
        capital_1.append(capital_1[-1] * (1 + f_1 * flips_1[i]))
        capital_2.append(capital_2[-1] * (1 + f_2 * flips_2[i]))
        capital_3.append(capital_3[-1] * (1 + f_3 * flips_3[i]))
        
    return capital_1, capital_2, capital_3, f_2

steps = 500
safe, kelly, degen, f_k = kelly_sim(p=0.6, steps=steps)

plt.figure(figsize=(12, 6))

plt.yscale('log')

plt.plot(safe, label='5%', color='blue', linewidth=2)
plt.plot(kelly, label='kelly', color='green', linewidth=3)
plt.plot(degen, label='40%', color='red', linewidth=2)

plt.axhline(1000, color='black', linestyle='--', label="starting capital")

plt.xlabel("no. of steps", fontsize=12)
plt.ylabel("capital - log scale", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3, which="both")
plt.tight_layout()
plt.show()

print(safe[-1])
print(kelly[-1])
print(degen[-1])
