import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Roboto'
matplotlib.rcParams['font.weight'] = 'light'

x = np.linspace(-5, 5, 400)

betas = [0.25, 0.5, 1.0, 2.0, 5.0]
colors = ["#cccccc", "#9ecae1", "#4292c6", "#2171b5", "#08306b"]

fig, ax = plt.subplots(figsize=(7, 6.5))

for beta, color in zip(betas, colors):
    p = 1.0 / (1.0 + np.exp(-beta * x))
    ax.plot(x, p, label=f"$\\beta={beta}$", linewidth=2, color=color)

ax.axhline(0.5, linestyle=":", color="#888888", linewidth=1)
ax.axvline(0.0, linestyle=":", color="#888888", linewidth=1)

ax.set_xlabel("$r(a) - r(b)$", fontsize=24)
ax.set_ylabel("$P(a \\succ b)$", fontsize=24)
ax.tick_params(axis='both', labelsize=20)
ax.legend(fontsize=20, loc="lower right", title="Rationality", title_fontsize=20)
ax.set_ylim(-0.05, 1.05)
ax.xaxis.set_major_locator(plt.MaxNLocator(6))
ax.yaxis.set_major_locator(plt.MaxNLocator(6))
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig("images/bradley_terry.pdf", bbox_inches="tight", transparent=True)
print("Saved images/bradley_terry.pdf")
