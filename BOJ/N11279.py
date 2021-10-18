import heapq
import sys

input = sys.stdin.readline 

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q, -x)
    elif x == 0:
        if q:
            value = -heapq.heappop(q)
            print(value)
        else:
            print(0)

