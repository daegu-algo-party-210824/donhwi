# 서로소인지 판별

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * n
for i in range(n):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] and i < j: # 입력이 대칭이므로 union이 불필요하게 2번 수행됨
            union_parent(parent, i, j)

result = True
cities = list(map(int, input().split()))
root = find_parent(parent, cities[0]-1)

for city in cities[1:]:
    if root != find_parent(parent, city-1):   # index 맞추기
        result = False
        break

if result:
    print("YES")
else:
    print("NO")

"""
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
"""