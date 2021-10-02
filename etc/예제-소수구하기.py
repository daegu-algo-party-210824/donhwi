import math, sys

input = sys.stdin.readline

m, n = map(int, input().split())

primes = [True] * (n+1)
primes[0] = False
primes[1] = False

for i in range(2, int(math.sqrt(n)) + 1):
    if primes[i] == True:
        j = 2
        while i * j <= n:
            primes[i*j] = False
            j += 1

for i in range(m, n+1):
    if primes[i]:
        print(i)
