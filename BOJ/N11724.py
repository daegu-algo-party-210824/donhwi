"""
BOJ N11724 연결요소의 개수
BFS or DFS 
"""

import sys
from collections import deque

# sys.setrecursionlimit(10000)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = 1

# def dfs(v):
#     visited[v] = 1
#     for i in graph[v]:
#         if visited[i] == 0:
#             dfs(i)

count = 0
for i in range(1, n+1):
    if visited[i] == 0:
        # dfs(i)
        bfs(i)
        count += 1

print(count)