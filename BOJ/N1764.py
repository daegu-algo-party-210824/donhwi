"""
set 활용 단순 구현
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

set1 = set()
set2 = set()

for _ in range(n):
    set1.add(input().rstrip())

for _ in range(m):
    set2.add(input().rstrip())

results = list(set1.intersection(set2))
results.sort()

print(len(results))
for result in results:
    print(result)

