import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm, ttest_ind

rng = np.random.default_rng(42)
mu = 4
x_pois = np.arange(0, 16)

pois_rv = poisson(mu=mu)

pmf_pois = pois_rv.pmf(x_pois)
cdf_pois = pois_rv.cdf(x_pois)
samples_pois = pois_rv.rvs(size=1000, random_state=rng)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))
axes[0].stem(x_pois, pmf_pois, basefmt=" ")
axes[0].set_title("Poisson PMF")
axes[0].set_xlabel("x")
axes[0].set_ylabel("P(X = x)")

axes[1].step(x_pois, cdf_pois, where="post")
axes[1].set_title("Poisson CDF")
axes[1].set_xlabel("x")
axes[1].set_ylabel("P(X <= x)")
axes[2].hist(samples_pois, bins=np.arange(-0.5, samples_pois.max() + 1.5, 1), density=True)
axes[2].set_title("Poisson Histogram (1000 samples)")
axes[2].set_xlabel("x")
axes[2].set_ylabel("Relative frequency")
plt.tight_layout()
plt.show()
