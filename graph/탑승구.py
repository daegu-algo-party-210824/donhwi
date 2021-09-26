# 서로소 집합 활용

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

import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

parent = [0] * (g+1)
for i in range(g+1):
    parent[i] = i

count = 0
gates = []

for _ in range(p):
    gates.append(int(input()))

for gate in gates:
    gate_parent = find_parent(parent, gate)
    if gate_parent == 0:
        break
    union_parent(parent, gate_parent, gate_parent-1)
    count += 1


print(count)

"""
4
6
2
2
3
3
4
4
"""



