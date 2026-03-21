#!/usr/bin/python

from math import ceil,sqrt
@profile
def gen_primes(n):
    l = range(2,n)
    primes = []
    for j in range(0,len(l)):
        p = True
        for d in primes:
            if(d > sqrt(l[j])):
                break
            if(l[j] % d == 0):
                p = False
                break;
        if(p):
            primes.append(l[j])

    return primes

@profile
def factorize(n,primes):
    factors = []
    init_n = n
    for p in primes:
        while(n%p == 0):
            n = n/p
            factors.append(p)
        if(p > sqrt(n)):
            break
    if(n > 1):
        factors.append(n)
    return factors

    
def phi(n,primes):
    factors = factorize(n,primes)
    p = 1

    for i in range(2,n):
        flag = True
        for f in factors:
            if i%f == 0:
                flag = False
                break
        if flag:
            p+=1
    return p

@profile
def fast_phi(n,primes):
    factors = factorize(n,primes)
    phi = factors[0]-1
    for i in range(1,len(factors)):
        if(factors[i] == factors[i-1]):
            phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
        else:
            phi *= (factors[i]-1)
    return phi

primes = gen_primes(1000)
m = 10000
#m = 8
fraq = 0
for i in range(2,m+1):
    fraq += fast_phi(i,primes)

print(fraq)


"""
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    50                                           @profile
    51                                           def fast_phi(n,primes):
    52      9999      71472.0      7.1     86.0      factors = factorize(n,primes)
    53      9999       1107.0      0.1      1.3      phi = factors[0]-1
    54     31985       3723.0      0.1      4.5      for i in range(1,len(factors)):
    55     21986       2735.0      0.1      3.3          if(factors[i] == factors[i-1]):
    56      7685       1102.0      0.1      1.3              phi *= (factors[i]-1)*(factors[i])/(factors[i]-1)
    57                                                   else:
    58     14301       1893.0      0.1      2.3              phi *= (factors[i]-1)
    59      9999       1107.0      0.1      1.3      return phi
The bottleneck is the call to factorize, which takes 86% of the time. The next most expensive line is the loop over the factors, which takes 4.5% of the time. The other lines take negligible time in comparison."""