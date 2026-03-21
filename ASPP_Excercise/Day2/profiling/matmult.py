import random
N = 250


def make_matrix(rows, cols):
    return [[random.randint(0, 100) for _ in range(cols)] for _ in range(rows)]


@profile
def matmult(X, Y):
    result = [[0] * len(Y[0]) for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]

    return result


def main():
    X = make_matrix(N, N)
    Y = make_matrix(N, N + 1)
    result = matmult(X, Y)

    for r in result:
        print(r)


if __name__ == "__main__":
    main()

'''
Total time: 3.72804 s
File: matmult.py
Function: matmult at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           @profile
    11                                           def matmult(X, Y):
    12         1         41.0     41.0      0.0      result = [[0] * len(Y[0]) for _ in range(len(X))]
    13                                           
    14       251         28.0      0.1      0.0      for i in range(len(X)):
    15     63000       6383.0      0.1      0.2          for j in range(len(Y[0])):
    16  15750250    1590961.0      0.1     42.7              for k in range(len(Y)):
    17  15687500    2130618.0      0.1     57.2                  result[i][j] += X[i][k] * Y[k][j]
    18                                           
    19         1          7.0      7.0      0.0      return result
    result[i][j] += X[i][k] * Y[k][j] is the bottleneck, taking 57.2% of the time. The next most expensive line is the loop over k, which takes 42.7% of the time. The other lines take negligible time in comparison.
    '''