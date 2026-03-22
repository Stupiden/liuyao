import numpy as np
from numpy.lib.stride_tricks import as_strided

# a
p = np.array([
    [1.0, 2.0, 10],
    [3.0, 4.0, 20],
    [5.0, 6.0, 30],
    [7.0, 8.0, 40]
])

z = p[:, 2]

z = z.reshape(-1, 1)

# Normalize
p_normalized = p / z

print(p_normalized)

# b
a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

diag = a[[0, 1, 2], [0, 1, 2]]

print(diag)

# c
import numpy as np

a = np.random.rand(10, 3)

diff = np.abs(a - 0.75)

j = np.argmin(diff, axis=1)

closest = a[np.arange(a.shape[0]), j]

print("Array:\n", a)
print("Indices:", j)
print("Closest values:", closest)

# d
x = np.empty((10, 8, 6))
idx0 = np.zeros((3, 8)).astype(int)
idx1 = np.zeros((3, 1)).astype(int)
idx2 = np.zeros((1, 1)).astype(int)

y = x[idx0, idx1, idx2]
print(y.shape)

# e
x = np.arange(12, dtype=np.int32).reshape((3, 4))

z = as_strided(
    x,
    shape=(2, 3, 2, 2),
    strides=(16, 4, 16, 4)
)

print(z)