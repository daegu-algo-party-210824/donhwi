import sys, heapq
input = sys.stdin.readline

n = int(input())

q = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if q:
            min_value = heapq.heappop(q)
            print(min_value[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(x), x))
