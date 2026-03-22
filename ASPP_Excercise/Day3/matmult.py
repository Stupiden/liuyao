import numpy as np

N = 250

X = np.random.randint(0, 101, size=(N, N))
Y = np.random.randint(0, 101, size=(N, N + 1))

# Matrix multiplication
result = X @ Y   # same as np.dot(X, Y)

for row in result:
    print(row)