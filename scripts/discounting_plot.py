import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Roboto'
matplotlib.rcParams['font.weight'] = 'light'

d = np.linspace(0, 20, 200)

k = 0.5
hyperbolic = 1 / (1 + k * d)

gamma = 0.8
exponential = gamma ** d

no_discount = np.ones_like(d)

fig, ax = plt.subplots(figsize=(7, 6.5))
ax.plot(d, no_discount, label="No discounting", linewidth=2, linestyle="--", color="#888888")
ax.plot(d, exponential, label=f"Exponential ($\\gamma={gamma}$)", linewidth=2, color="#2196F3")
ax.plot(d, hyperbolic, label=f"Hyperbolic ($k={k}$)", linewidth=2, color="#E91E63")

ax.set_xlabel("Delay $d$", fontsize=24)
ax.set_ylabel("Discount factor", fontsize=24)
ax.tick_params(axis='both', labelsize=20)
ax.legend(fontsize=22, loc="right")
ax.set_ylim(-0.05, 1.15)
ax.xaxis.set_major_locator(plt.MaxNLocator(6))
ax.yaxis.set_major_locator(plt.MaxNLocator(6))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("images/discounting.svg", bbox_inches="tight", transparent=True)
print("Saved images/discounting.svg")
