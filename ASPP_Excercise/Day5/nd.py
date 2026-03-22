import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm, ttest_ind

rng = np.random.default_rng(42)
mu_norm = 0
sigma_norm = 1

norm_rv = norm(loc=mu_norm, scale=sigma_norm)

x_norm = np.linspace(-4, 4, 400)
pdf_norm = norm_rv.pdf(x_norm)   # continuous case: PDF
cdf_norm = norm_rv.cdf(x_norm)
samples_norm = norm_rv.rvs(size=1000, random_state=rng)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# PDF
axes[0].plot(x_norm, pdf_norm)
axes[0].set_title("Normal PDF")
axes[0].set_xlabel("x")
axes[0].set_ylabel("f(x)")

# CDF
axes[1].plot(x_norm, cdf_norm)
axes[1].set_title("Normal CDF")
axes[1].set_xlabel("x")
axes[1].set_ylabel("P(X <= x)")

# Histogram of realizations
axes[2].hist(samples_norm, bins=30, density=True, alpha=0.8)
axes[2].plot(x_norm, pdf_norm)  # optional: overlay theoretical PDF
axes[2].set_title("Normal Histogram (1000 samples)")
axes[2].set_xlabel("x")
axes[2].set_ylabel("Density")

plt.tight_layout()
plt.show()