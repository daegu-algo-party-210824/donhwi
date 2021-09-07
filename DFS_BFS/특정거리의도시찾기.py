import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().rstrip().split(" "))
INF = 999999999
distances = [INF] * (n + 1)
graph = [[] for _ in range(n+1)]

# 인접리스트 방식으로 연결되어 있는 노드를 표시
for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[start].append(end)

def bfs(v, distances):
    queue = deque()
    queue.append(v)
    distances[v] = 0

    while queue:
        v = queue.popleft()
        for i in range(len(graph[v])):
            nv = graph[v][i]
            if distances[nv] is INF: # 아직 방문하지 않았으면
                queue.append(nv)

            if distances[nv] > distances[v] + 1:
                distances[nv] = distances[v] + 1

bfs(x, distances)

count = 0

for index in range(1, len(distances)):
    if distances[index] == k:
        print(index)
        count += 1

if count == 0:
    print(-1)