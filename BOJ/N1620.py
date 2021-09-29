import sys

input = sys.stdin.readline

n, m = map(int, input().split())

pm = [""]
pm_dict = {}

for i in range(n):
    name = input().rstrip()
    pm.append(name)
    pm_dict[name] = i+1

for i in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(pm[int(q)])
    else:
        print(pm_dict[q])
