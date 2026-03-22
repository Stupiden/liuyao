import ASPP_Excercise.Day3.numpy_practice as np

Z = np.zeros(10)
Z[4] = 1
print(Z)

Z = np.arange(10, 50)
print(Z)

Z = Z[::-1]
print(Z)

Z = np.arange(9).reshape(3, 3)
print(Z)

a = [1,2,0,0,4,0]
indices = np.nonzero(a)[0]
print(indices)

random_vector = np.random.random(30)
mean_value = np.mean(random_vector)
print(mean_value)

Z = np.ones((5, 5))
Z[1:-1, 1:-1] = 0
print(Z)

Z = np.zeros((8, 8))
Z[::2, ::2] = 1
Z[1::2, 1::2] = 1
print(Z)

Z = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
print(Z)

Z = np.arange(11)
Z[(Z > 3) & (Z < 8)] *= -1
print(Z)

Z = np.random.random(10)
Z.sort()
print(Z)

A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.array_equal(A, B)
print(equal)

Z = np.arange(10, dtype=np.int32)
Z **= 2
print(Z.dtype)

A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
