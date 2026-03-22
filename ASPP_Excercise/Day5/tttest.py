import numpy as np
from scipy.stats import ttest_ind

rng = np.random.default_rng(42)

data1 = rng.normal(loc=0, scale=1, size=100)
data2 = rng.normal(loc=0, scale=1, size=100)

t_stat, p_value = ttest_ind(data1, data2, equal_var=True)

print("Case 1 (same distribution):")
print("t =", t_stat)
print("p =", p_value)

if p_value < 0.05:
    print("Reject H0: means are different")
else:
    print("Fail to reject H0: no evidence of difference")

print()